from django.conf.urls import url,include

from apps.admins.views import account
from apps.admins.views import commodity
from apps.admins.views import uploads

# from rest_framework import routers
#
# routers = routers.DefaultRouter()
# routers.register('course',course.CourseModelView)


urlpatterns = [
    url(r'^auth/$', account.AuthView.as_view()),

    url(r'^commodity/$',commodity.CommodityView.as_view({"get":"list","post":"add"})),
    url(r'^commodity/(?P<pk>\d+)/$',commodity.CommodityView.as_view({"get":"retrieve"})),

    url(r'^upload/$',uploads.UploadView.as_view()),
]