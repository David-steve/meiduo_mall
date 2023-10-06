from django.urls import path, re_path

from apps.users.views import UserNameCount

urlpatterns = [
    # 正则路径
    # re_path(r'username/(?P<username>[0-9a-zA-Z]{5,20})/count', UserNameCount.as_view()),
    # 转换器
    path(r'usernames/<username_converter:username>/count/', UserNameCount.as_view()),
]
