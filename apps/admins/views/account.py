from rest_framework.views import APIView
from rest_framework.response import Response
from apps import models
from microapp.settings import SECRET_KEY
from hashlib import md5
import uuid,time


class AuthView(APIView):
    authentication_classes = []

    def post(self,request,*args,**kwargs):
        '''
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code':1000,}
        user = request.data.get('user')
        pwd = md5(request.data.get('pwd').encode('utf-8')+SECRET_KEY.encode('utf-8')).hexdigest()
        user = models.Admin.objects.filter(username=user,password=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            token = models.AdminToken.objects.filter(admin_id=user.id).first()
            if time.time() - token.addtime > 86400:
                uid = str(uuid.uuid4())
                models.AdminToken.objects.update_or_create(admin_id=user.id,defaults={"token":uid,"addtime":time.time()})
                ret['token'] = uid
            else:
                ret['token'] = token.token
        return Response(ret)
