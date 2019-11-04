from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from apps.admins.auth.auth import *
from microapp.settings import STATIC_URL
import imghdr,os


class UploadView(APIView):
    parser_classes = (MultiPartParser,)
    # APIView.authentication_classes = [Auth, ]  # 认证模块

    def post(self,request,*args,**kwargs):
        ret = {"code":1000,"msg":""}
        # 获取多个file
        files = request.FILES.getlist('img',None)
        if files:  # 验证是否有图片文件上传

            img_dic = {}
            for file_obj in files:
                imgType = imghdr.what(file_obj)  # 验证是否为真图片
                if imgType:
                    with open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/static/temporaryfolder/'+file_obj.name,'wb+') as f:
                        for content in file_obj.chunks():
                            f.write(content)
                        f.close()

                    img_dic[file_obj.name] = 'http://118.89.54.143:8000/static/temporaryfolder/'.encode('utf-8')+file_obj.name.encode('utf-8')
                else:
                    ret["code"] = 2001
                    ret["msg"] = "上传图片失败！"
                    return Response(ret)
            ret["msg"] = "上传图片成功！"
            ret["img"] = img_dic
        else:
            ret["code"] = 2001
            ret["msg"] = "上传图片失败！"
        return Response(ret)
