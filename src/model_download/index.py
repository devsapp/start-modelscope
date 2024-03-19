import os 
from datetime import datetime
from threading import Timer
from modelscope.hub.api import HubApi
from modelscope.hub.snapshot_download import snapshot_download

finish_flag = False
def loop_log():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts)
    if finish_flag == True:
        return
    t = Timer(10, loop_log)
    t.start()

def handler(event, context):
    model_id = os.getenv('MODEL_ID', '')
    revision = os.getenv('MODEL_VERSION', '')
    cache_dir = os.getenv('MODELSCOPE_CACHE', '')
    sdk_token = os.getenv('MODELSCOPE_TOKEN', '')
    # avoid no response bytes in long periods
    loop_log()
    # login first.
    HubApi().login(sdk_token)
    if len(revision) > 0:
        snapshot_download (model_id =model_id, 
                           revision =revision,
                           cache_dir = cache_dir)
    else:
         snapshot_download (model_id =model_id, 
                            cache_dir = cache_dir)
    print("download model scuccess!")
    finish_flag = True
