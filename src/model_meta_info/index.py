import os 
from modelscope.hub.api import HubApi
from modelscope.hub.snapshot_download import snapshot_download

def handler(event, context):
    served_model_name = os.getenv('SERVED_MODEL_NAME', '')

    return {'served_model_name': served_model_name}