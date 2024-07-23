import os 
from modelscope.hub.api import HubApi
from modelscope.hub.snapshot_download import snapshot_download

def handler(event, context):
    model_id = os.getenv('MODEL_ID', '')
    revision = os.getenv('MODEL_VERSION', '')
    cache_dir = os.getenv('MODELSCOPE_CACHE', '')
    sdk_token = os.getenv('MODELSCOPE_TOKEN', '')
    image_tag = os.getenv('IMAGE_TAG', '')
    gguf_file = os.getenv('GGUF_FILE', '')

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
        os.system('pip install --default-timeout=100 modelscope==1.16')
        command_download_ollama = f'modelscope download --model=modelscope/ollama-linux --local_dir {cache_dir}/ollama-linux'
        os.system(command_download_ollama)

        command_download_model = f'modelscope download --model={model_id} --local_dir {cache_dir} {gguf_file}'
        os.system(command_download_model)

        print("download model scuccess!")