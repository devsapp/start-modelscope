import os
import json

os.system('pip config set global.index-url https://mirrors.cloud.aliyuncs.com/pypi/simple')
os.system('pip config set install.trusted-host mirrors.cloud.aliyuncs.com')
os.system('pip3 install flask')

from flask import Flask, request


model_task = os.getenv('TASK', '')
app = Flask(__name__)

def get_task_input_examples(task):
    current_work_dir = os.path.dirname(__file__)
    with open(current_work_dir + '/data/data/pipeline_inputs.json', 'r') as f:
        input_examples = json.load(f)
    if task in input_examples:
        return input_examples[task]
    return None


@app.route('/schemas', methods=['GET'])
def get_schemas():
    request_id = request.headers.get("x-fc-request-id", "")
    schemas_task = request.args.get("task", model_task)

    if not schemas_task:
        err_ret = {
            'Code': 400,
            'Message': "failed",
            'Data': "param task is null",
            "RequestId": request_id,
            "Success": False
        }
        return err_ret, 400, [("x-fc-status", "400")]

    print("[INFO] get schemas by task: " + schemas_task)
    result = get_task_input_examples(schemas_task)
    if not result:
        err_ret = {
            'Code': 400,
            'Message': "failed",
            'Data': "param task is invalid.",
            "RequestId": request_id,
            "Success": False
        }
        return err_ret, 400, [("x-fc-status", "400")]

    return {
               'Code': 200,
               'Message': "",
               'Data': result,
               "RequestId": request_id,
               "Success": True
           }, 200, [("Content-Type", "application/json")]


if __name__ == '__main__':
    os.system('mkdir data; cd data; wget https://modelscope.oss-cn-beijing.aliyuncs.com/swingdeploy/deploy.tar; tar xvf deploy.tar')
    app.run(debug=False, host='0.0.0.0', port=9000)
