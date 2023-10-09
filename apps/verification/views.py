from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection
from redis import Redis

from lib.captcha.captcha import captcha


class ImageCodesView(View):
    def get(self, request, uuid):
        text, image = captcha.generate_captcha()

        redis_cli: Redis = get_redis_connection('code')
        redis_cli.setex(uuid, 100, text)

        return HttpResponse(content=image, content_type='image/jpeg')
        # return HttpResponse("hello")
        pass


class SMSCodeView(View):
    def get(self, request, phone):
        pass
