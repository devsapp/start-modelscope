import os 
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

    # login first.
    HubApi().login(sdk_token)
    if image_tag == 'fc-deploy-common-v17.3.3':
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
        api = HubApi()
        latest_ollama = api.list_model_revisions(model_id='modelscope/ollama-linux')[0]
        os.system(f'modelscope download --model=modelscope/ollama-linux --local_dir {cache_dir}/ollama-linux --revision {latest_ollama}')

        command_download_model = f'modelscope download --model={model_id} --local_dir {cache_dir} {sub_model_file}'
        os.system(command_download_model)

        os.system(f'cd {cache_dir}/ollama-linux && chmod 777 ./ollama-modelscope-install.sh && ./ollama-modelscope-install.sh')
        os.system(f'OLLAMA_MODELS={cache_dir} OLLAMA_HOST=127.0.0.1:9000 ollama serve &')
        os.system(f'wget {template_file_url} -O /home/modelfile')

        os.system(f'echo  {cache_dir}/{sub_model_file}')
        os.system(f'ln -snf {cache_dir}/{sub_model_file} /home/{sub_model_file}')

        with open('/home/modelfile', 'r') as f_in, open('/home/ModelFile', 'w') as f_out:
            lines = f_in.readlines()
            assert lines[0].strip() == 'FROM {gguf_file}', '请不要修改配置文件第一行 `FROM {gguf_file}`。'
            lines[0] = lines[0].replace('{gguf_file}', f'{sub_model_file}')
            f_out.writelines(lines)

        os.system(f'OLLAMA_HOST=0.0.0.0:9000 ollama create {model_id} --file /home/ModelFile')

        print("download model scuccess!")