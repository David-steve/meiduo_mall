from django.urls import path, re_path

from apps.users.views import UserNameCount

urlpatterns = [
    # 正则路径
    re_path(r'username/(?P<username>\w+)/count', UserNameCount.as_view()),
]
