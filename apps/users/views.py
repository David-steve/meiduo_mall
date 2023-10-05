import logging
import re

from django.http import JsonResponse


# Create your views here.
from django.views import View

from apps.users.models import User


class UserNameCount(View):
    def get(self, request, username):
        if not re.match(r'\w{5,20}', username):
            logger = logging.getLogger(__name__)
            logger.info(f"username: '{username}' does not match rules")

            return JsonResponse({'code': 0, 'count': 0, 'errmsg': 'do not match rules'})

        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})
