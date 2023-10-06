import json
import logging
import re

from django.http import JsonResponse

# Create your views here.
from django.views import View

from apps.users.models import User


class UserNameCount(View):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()

        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})


class MobileCount(View):
    def get(self, request, phone):
        count = User.objects.filter(phone=phone).count()

        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})


class RegisterView(View):
    def post(self, request):
        json_str = request.body
        info_dict = json.loads(json_str)

        username = info_dict.get("username")
        password = info_dict.get("password")
        password2 = info_dict.get("password2")
        mobile = info_dict.get("mobile")
        allow = info_dict.get("allow")

        # 不要相信前端传过来的所有数据，后端要自己验证一遍
        if not all([username, password, password2, mobile, allow]):
            return JsonResponse({'code': 400, 'errmsg': '参数不全'})

        # 验证用户名是否符合规则，是否重复
        if not re.match(r'[\da-zA-Z_]{5,20}', username) or User.objects.filter(username=username).count():
            return JsonResponse({'code': 400, 'errmsg': '用户名不符合规则'})

        if password != password2:
            return JsonResponse({'code': 400, 'errmsg': '密码不一致'})
        if not re.match(r'[\d]{11}$', mobile) or User.objects.filter(phone=mobile).count():
            return JsonResponse({'code': 400, 'errmsg': '手机号码不符合规则'})

        User.objects.create_user(username=username, password=password, phone=mobile)

        return JsonResponse({'code': 0, 'errmsg': 'ok'})
