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

    return {'served_model_name': served_model_name}