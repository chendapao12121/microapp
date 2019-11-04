from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apps import models
import time

class Auth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')  # = request.GET
        obj = models.AdminToken.objects.filter(token=token).first()
        if not obj:
            # obj = models.UserToken.objects.filter(token=token).first()
            # if not obj:
            raise AuthenticationFailed({'code':1001,'error':'用户认证失败'})
        else:
            if time.time() - models.AdminToken.objects.filter(token=token).first().addtime > 86400:
                raise AuthenticationFailed({'code': 1002, 'error': '用户已过期！请重新登录！'})
        return (obj.admin.username,obj)
