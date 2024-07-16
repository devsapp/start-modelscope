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
    modelfile = os.getenv('MODELFILE', '')
    family = os.getenv('MODEL_FAMILY', '')
    served_model_name = os.getenv('SERVED_MODEL_NAME', '')

    cmd = f'cd {cache_dir}/ollama-linux && sudo chmod 777 ./ollama-modelscope-install.sh && ./ollama-modelscope-install.sh'
    os.system(cmd)
    cmd = 'ollama serve &'
    os.system(cmd)

    if modelfile and len(modelfile):
        os.system(f'cat {modelfile} > {cache_dir}/ModelFile')
    elif family and len(family):
        os.system(f'wget https://modelscope.oss-cn-beijing.aliyuncs.com/llm_template/ollama/{family}.modelfile')
        command_gen_modelfile = f'cat {family}.modelfile | sed "s/' + '{gguf_file}' + f'/{gguf_file}/" > ./ModelFile'
        os.system(command_gen_modelfile)
    else:
        raise ValueError(f'modelfile 和 model_family至少需要配置一个。用于ollama模型初始化。')
    
    # run ollama
    cmd = f'ollama create {served_model_name} --file ./ModelFile'
    os.system(cmd)
    cmd = f'ollama run {served_model_name}'
    os.system(cmd)