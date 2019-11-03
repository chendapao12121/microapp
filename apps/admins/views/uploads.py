from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from apps.admins.auth.auth import *
import imghdr


class UploadView(APIView):
    parser_classes = (MultiPartParser,)
    # APIView.authentication_classes = [Auth, ]  # 认证模块

    def post(self,request,*args,**kwargs):
        ret = {"code":1000,"msg":""}
        # 获取多个file
        files = request.FILES.getlist('img',None)
        if files:  # 验证是否有图片文件上传
            for file_obj in files:
                imgType = imghdr.what(file_obj)  # 验证是否为真图片
                if imgType:
                    with open('apps/static/temporaryfolder/'+file_obj.name,'wb+') as f:
                        for content in file_obj.chunks():
                            f.write(content)
                        f.close()
                    ret[file_obj.name] = 'apps/static/temporaryfolder/'+file_obj.name
                else:
                    ret["code"] = 2001
                    ret["msg"] = "上传图片失败！"
                    return Response(ret)
            ret["msg"] = "上传图片成功！"
        else:
            ret["code"] = 2001
            ret["msg"] = "上传图片失败！"
        return Response(ret)
