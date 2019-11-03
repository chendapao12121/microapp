from django.conf.urls import url,include

from apps.admins.views import account

# from rest_framework import routers
#
# routers = routers.DefaultRouter()
# routers.register('course',course.CourseModelView)


urlpatterns = [
    url(r'^admin/',include('apps.admins.urls')),
]