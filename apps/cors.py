class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):

    def process_response(self,request,response):
        # 添加响应头
        # 允许你的域名来获取数据
        # response['Access-Control-Allow-Origin'] = "*"  # 允许任何请求数据

        # 允许你携带Content-Type请求头
        # 请求头定死的，不能写*
        # response['Access-Control-Allow-Headers'] = "Content-Type"

        # 允许发送delete，put请求
        # response['Access-Control-Allow-Methods'] = "PUT,DELETE"

        response['Access-Control-Allow-Origin'] = "*"  # 允许任何请求数据
        if request.method == "OPTIONS":
            response['Access-Control-Allow-Headers'] = "Content-Type"
            response['Access-Control-Allow-Methods'] = "PUT,DELETE"
        return response
