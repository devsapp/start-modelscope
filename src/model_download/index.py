import os
import traceback
from modelscope.hub.api import HubApi
from modelscope.hub.snapshot_download import snapshot_download

def handler(event, context):
    model_id = os.getenv('MODEL_ID', '')
    revision = os.getenv('MODEL_VERSION', '')
    cache_dir = os.getenv('MODELSCOPE_CACHE', '')
    sdk_token = os.getenv('MODELSCOPE_TOKEN', '')
    image_tag = os.getenv('IMAGE_TAG', '')
    sub_model_file = os.getenv('SUB_MODEL_FILE', '')
    template_file_url = os.getenv('TEMPLATE_FILE_URL', '')
    backend = os.getenv('MODEL_BACKEND', 'pipeline')

    # login first.
    try:
        # model cache url
        api = HubApi()
        api.login(sdk_token)
    except BaseException as e:
        print(f'[INFO] Download model from www.modelscope.cn, cache failed: {e}, {traceback.print_exc()}')
        os.environ['MODELSCOPE_DOMAIN'] = 'www.modelscope.cn'
        api = HubApi()
        api.login(sdk_token)

    if backend == 'pipeline':
        if len(revision) > 0:
            snapshot_download (model_id =model_id,
                            revision =revision,
                            cache_dir = cache_dir)
        else:
            snapshot_download (model_id =model_id, 
                                cache_dir = cache_dir)
        print("download model scuccess!")
    else:
        os.system('pip config set global.index-url https://mirrors.cloud.aliyuncs.com/pypi/simple')
        os.system('pip config set install.trusted-host mirrors.cloud.aliyuncs.com')
        os.system('pip install --default-timeout=100 modelscope==1.16')

        # using latest ollama
        print('[INFO] Downloading and installing the latest ollama. ')
        latest_ollama = api.list_model_revisions(model_id='modelscope/ollama-linux')[0]
        os.system(f'modelscope download --model=modelscope/ollama-linux --local_dir {cache_dir}/ollama-linux --revision {latest_ollama}')

        print(f'[INFO] Downloading model file. ')
        command_download_model = f'modelscope download --model={model_id} --local_dir {cache_dir} {sub_model_file}'
        os.system(command_download_model)

        os.system(f'cd {cache_dir}/ollama-linux && chmod 777 ./ollama-modelscope-install.sh && ./ollama-modelscope-install.sh')
        os.system(f'OLLAMA_MODELS={cache_dir} OLLAMA_HOST=127.0.0.1:9000 ollama serve &')
        os.system(f'wget {template_file_url} -O /home/modelfile')

        os.system(f'echo  {cache_dir}/{sub_model_file}')
        os.system(f'ln -snf {cache_dir}/{sub_model_file} /home/{sub_model_file}')

        with open('/home/modelfile', 'r') as f_in, open('/home/ModelFile', 'w') as f_out:
            lines = f_in.readlines()
            if not len(lines):
                print(f'[ERROR] Failed to download {template_file_url}.')
            lines[0] = 'FROM {gguf_file}\n'.replace('{gguf_file}', f'{sub_model_file}')
            print(f'[INFO] modelfile:\n{lines}')
            f_out.writelines(lines)

        print('[INFO] Create the model with ollama in advance and cache it.')

        os.system(f'OLLAMA_HOST=0.0.0.0:9000 ollama create {model_id} --file /home/ModelFile')

        print("download model scuccess!")