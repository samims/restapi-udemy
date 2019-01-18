from django.conf.urls import url

from .views import (
    UpdateModeDetailAPIView,
    UpdateModelListAPIView,
)


urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view(), ),
    url(r'^(?P<id>\d+)/$', UpdateModeDetailAPIView.as_view()),
]