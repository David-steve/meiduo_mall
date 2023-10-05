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
