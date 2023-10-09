from django.urls import path

from apps.verification.views import ImageCodesView

urlpatterns = [
    path('image_codes/<uuid>/', ImageCodesView.as_view()),
]
