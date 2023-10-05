"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


# 测试logger用
def log(request):
    logger = logging.getLogger(__name__)
    content = request.GET

    name = content["name"]
    logger.debug(f"{name} 登录网站")
    logger.info(f"{name} 退出网站")
    logger.warning("缓存不足")
    logger.error("该文件不存在")

    return HttpResponse("log")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', log),
    path('', include('apps.users.urls'))
]
