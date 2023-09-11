import zhipuai

# your api key
# zhipuai.api_key = "9be62b67024a7efa008c48313f2ba057.bsU8jbZ6tGhnMU5U"

class ChatGLMApiLLMClient:
    def __init__(self, model_name: str, api_key: str):

        zhipuai.api_key = api_key
        self.api_key= api_key


    def invoke_example(self):
        response = zhipuai.model_api.invoke(
            model="chatglm_pro",
            prompt=[{"role": "user", "content": "人工智能"}],
            top_p=0.7,
            temperature=0.9,
        )
        print(response)

    def async_invoke_example(self):
        response = zhipuai.model_api.async_invoke(
            model="chatglm_pro",
            prompt=[{"role": "user", "content": "人工智能"}],
            top_p=0.7,
            temperature=0.9,
        )
        print(response)

    '''
      说明：
      add: 事件流开启
      error: 平台服务或者模型异常，响应的异常事件
      interrupted: 中断事件，例如：触发敏感词
      finish: 数据接收完毕，关闭事件流
    '''

    def sse_invoke_example(self):
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_pro",
            prompt=[{"role": "user", "content": "人工智能"}],
            top_p=0.7,
            temperature=0.9,
        )

        for event in response.events():
            if event.event == "add":
                print(event.data)
            elif event.event == "error" or event.event == "interrupted":
                print(event.data)
            elif event.event == "finish":
                print(event.data)
                print(event.meta)
            else:
                print(event.data)

    def query_async_invoke_result_example(self):
        response = zhipuai.model_api.query_async_invoke_result("your task_id")
        print(response)

    def subscribe(self,messages):
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_std",
            prompt=messages,
            top_p=0.7,
            temperature=0.9,
        )

        for event in response.events():
            if event.event == "add":
                yield(event.data)
            elif event.event == "error" or event.event == "interrupted":
                yield(event.data)
            elif event.event == "finish":
                yield(event.data)
                print(event.meta)
            else:
                yield(event.data)

class SparkError(Exception):
    pass
