from PIL import Image
import gradio as gr
import io
import os
import requests
import base64
import random
import time


## global variables inherited from env
demo = None
model_id = os.getenv('MODEL_ID', '')
model_revision = os.getenv('MODEL_VERSION', '')
model_task = os.getenv('TASK', '')
api_url = os.getenv('API_URL')
title = "魔搭社区x函数计算 : 一键部署模型"
description = "本页面提供图形化方式调用部署后的魔搭模型，更多FAQ请见 [ModelScope一键部署模型：新手村实操FAQ篇](https://developer.aliyun.com/article/1307460?spm=5176.28261954.J_7341193060.1.43f42fdewvfTyq&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1307460._.ID_1307460-RL_%E9%AD%94%E6%90%AD%20%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0)"
article = '''
- 模型ID: [{}](https://www.modelscope.cn/models/{})
- 模型版本: {}
- 模型任务类型: {}
- 模型推理URL: {}/invoke'''.format(model_id, model_id, model_revision, model_task, api_url)

print("[debug] model_id=", model_id)
print("[debug] model_revision=", model_revision)
print("[debug] model_task=", model_task)
print("[debug] api_url=", api_url)

if model_task == None or len(model_task) == 0:
    gr.Warning("Missing necessary model task")
if api_url == None or len(api_url) == 0:
    gr.Warning("Missing necessary api url")
else:
    api_url += "/invoke"

## utils
def post_request(url, json):
    with requests.Session() as session:
        response = session.post(url,json=json,)
        return response

## model task setup handlers
def image_captioning_setup():
    def handler(url):
        if url == None or len(url) == 0:
            raise gr.Error("Missing necessary image url, please retry.")
        payload = {"input": {"image": url}}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json(), url
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs=["text", gr.Image(shape=(200, 200), height=200, width=200)],
                        examples=["https://xingchen-data.oss-cn-zhangjiakou.aliyuncs.com/maas/image-captioning/dress.png"],
                        title=title,
                        description=description,
                        article=article)

def image_portrait_stylization_setup():
    def handler(url):
        if url == None or len(url) == 0:
            raise gr.Error("Missing necessary image url, please retry.")
        payload = {"input": {"image": url}}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        status = response.json()["Code"]
        if status != 200:
            raise gr.Error("Inference response code is !200, please retry.")
        image_base64 = response.json()["Data"]["output_img"]
        if image_base64 == None or len(image_base64) == 0:
            raise gr.Error("Inference response image data(base64) is none, please retry.")
        image_raw = base64.b64decode(image_base64)
        if image_raw == None or len(image_raw) == 0:
            raise gr.Error("Inference response image data(raw) is none,please retry.")
        init_image = Image.open(io.BytesIO(image_raw))
        return url, init_image
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs=[gr.Image(height=300, width=300, label="original"),
                                 gr.Image(height=300, width=300, label="postprocess")],
                        examples=["https://modelscope.oss-cn-beijing.aliyuncs.com/demo/image-cartoon/cartoon.png"],
                        title=title,
                        description=description,
                        article=article)


def text_generation_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": text}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是",
                                  "今天天气如何",
                                  "你好"],
                        title=title,
                        description=description,
                        article=article)

def text_classification_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": text}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["这件衣服挺好看", "这件衣服挺太难看了"],
                        title=title,
                        description=description,
                        article=article)

def faq_question_answering_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": [text]}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["这件衣服挺好看", "这件衣服不好看"],
                        title=title,
                        description=description,
                        article=article)

def zero_shot_classification_setup():
    def handler(text, candidate_labels):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        if candidate_labels == None or len(candidate_labels) == 0:
            raise gr.Error("Missing necessary input candidate_labels, please retry.")
        payload = {"input": text, "parameters": {"candidate_labels": candidate_labels}}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs=["text", "text"],
                        outputs="text",
                        examples=[["世界那么大，我想去看看", "旅游, 故事, 游戏, 家居, 科技"]],
                        title=title,
                        description=description,
                        article=article)

def named_entity_recognition_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": text}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["eh 摇滚狗涂鸦拔印宽松牛仔裤 情侣款"],
                        title=title,
                        description=description,
                        article=article)

def word_segmentation_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": text}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["阿里巴巴集团的使命是让天下没有难做的生意"],
                        title=title,
                        description=description,
                        article=article)

def translation_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": text}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs="text",
                        examples=["阿里巴巴集团的使命是让天下没有难做的生意", "今天天气真不错"],
                        title=title,
                        description=description,
                        article=article)

def text_ranking_setup():
    def handler(source_sentence, sentences_to_compare1, sentences_to_compare2):
        if source_sentence == None or len(source_sentence) == 0:
            raise gr.Error("Missing necessary input source_sentence, please retry.")
        if sentences_to_compare1 == None or len(sentences_to_compare1) == 0 or sentences_to_compare2 == None or len(sentences_to_compare2) == 0:
            raise gr.Error("Missing necessary input sentences_to_compare, please retry.")
        payload = {"input": {"source_sentence": [source_sentence], "sentences_to_compare": [sentences_to_compare1, sentences_to_compare2]}}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs=["text", "text", "text"],
                        outputs="text",
                        examples=[["功和功率的区别", "功反映做功多少，功率反映做功快慢。", "什么是有功功率和无功功率?无功功率有什么用什么是有功功率和无功功率?无功功率有什么用电力系统中的电源是由发电机产生的三相正弦交流电,在交>流电路中,由电源供给负载的电功率有两种;一种是有功功率,一种是无功功率.", "优质解答在物理学中,用电功率表示消耗电能的快慢．电功率用P表示,它的单位是瓦特（Watt）,简称瓦（Wa）符号是W.电流在单位时间内做的功叫做电功率 以灯泡为例,电功率越大,灯泡越亮.灯泡的亮暗由电功率（实际功率）决定,不由通过的电流、电压、电能决定!"]],
                        title=title,
                        description=description,
                        article=article)

def chat_setup():
    def handler(message, history):
        if message == None or len(message) == 0:
            raise gr.Error("Missing necessary input message, please retry.")
        if history == None:
            history = []
        print("history:", history)
        messages = []
        for talk in history:
            talk_u = {"content":talk[0],"role":"user"}
            talk_a = {"content":talk[1],"role":"assistant"}
            messages.append(talk_u)
            messages.append(talk_a)
        messages.append({"content":message,"role":"user"})
        payload = {"input":{"messages":messages}, "parameters":{"do_sample":True,"max_length":1024}}
        print("payload:", payload)
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        response = response.json()

        # Compatible with different LLMs
        output = ""
        if response["Code"] != 200:
            output = "[internal error] Errmsg: " + response["Message"] + " RequestId: " + response["RequestId"]
        else:
            output = response["Data"]["message"]["content"]

        return output

    with gr.Blocks() as demo:
        gr.ChatInterface(fn=handler,
                         examples=["hello", "您好", "今天天气如何"],
                         title=title,
                         description=description)
        gr.Markdown(article)

    return demo

    #with gr.Blocks() as demo:
    #    chatbot = gr.Chatbot()
    #    msg = gr.Textbox()
    #    clear = gr.ClearButton([msg, chatbot])#

    #    def handler(message, chat_history):
    #        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    #        chat_history.append((message, bot_message))
    #        time.sleep(2)
    #        return "", chat_history

    #    msg.submit(handler, [msg, chatbot], [msg, chatbot])

    #return demo

def nli_seutp():
    def handler(text1, text2):
        if text1 == None or len(text1) == 0 or text2 == None or len(text2) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": [text1, text2]}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        return response.json()
    
    return gr.Interface(fn=handler,
                        inputs=["text", "text"],
                        outputs="text",
                        examples=[["这件衣服挺好看", "这件衣服不好看"]],
                        title=title,
                        description=description,
                        article=article)

def text_to_video_synthesis_setup():
    def handler(text):
        if text == None or len(text) == 0:
            raise gr.Error("Missing necessary input text, please retry.")
        payload = {"input": {"text": text}}
        response = post_request(api_url, json=payload)
        print("response:", response.json())
        status = response.json()["Code"]
        if status != 200:
            raise gr.Error("Inference response code is !200, please retry.")
        data_base64 = response.json()["Data"]["output_video"]
        if data_base64 == None or len(data_base64) == 0:
            raise gr.Error("Inference response video data(base64) is none, please retry.")
        data_raw = base64.b64decode(data_base64)
        if data_raw == None or len(data_raw) == 0:
            raise gr.Error("Inference response video data(raw) is none,please retry.")
        with open("/tmp/output.mp4", "wb") as out_file:
            out_file.write(data_raw)
        return "/tmp/output.mp4"
    
    return gr.Interface(fn=handler,
                        inputs="text",
                        outputs=gr.Video(height=400, width=400),
                        examples=["A panda eating bamboo on a rock.", "Robot dancing in times square.", "Tiny plant sprout coming out of the ground."],
                        title=title,
                        description=description,
                        article=article)

def default_setup():
    def default_callback():
        return "invalid model task"

    return gr.Interface(fn=default_callback, inputs=None, outputs="text", title="404", description="invalid model task")

## initiailzie
model_task_handlers = {
    # cv
    "image-captioning" : image_captioning_setup,
    "image-portrait-stylization" : image_portrait_stylization_setup,
    # nlp
    "text-generation" : text_generation_setup,
    "text-classification" : text_classification_setup,
    "faq-question-answering" : faq_question_answering_setup,
    "zero-shot-classification" : zero_shot_classification_setup,
    "named-entity-recognition" : named_entity_recognition_setup,
    "word-segmentation" : word_segmentation_setup,
    "translation" : translation_setup,
    "text-ranking" : text_ranking_setup,
    "chat" : chat_setup,
    "nli" : nli_seutp,
    # audio
    # multimodal
    "text-to-video-synthesis" : text_to_video_synthesis_setup,
    # science
    # default
    "default" : default_setup,
}

if model_task_handlers.get(model_task) == None:
    demo = model_task_handlers["default"]()
else:
    demo = model_task_handlers[model_task]()
    
demo.launch(server_name="0.0.0.0")
