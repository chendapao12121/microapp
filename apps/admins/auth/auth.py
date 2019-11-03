from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apps import models


class Auth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')  # = request.GET
        obj = models.AdminToken.objects.filter(token=token).first()
        if not obj:
            # obj = models.UserToken.objects.filter(token=token).first()
            # if not obj:
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.admin.username,obj)
