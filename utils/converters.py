from django.urls import converters


class UserNameConverters:
    regex = r'[0-9a-zA-Z]{5,20}'

    def to_python(self, value):
        return value
