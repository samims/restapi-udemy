from django.conf.urls import url
from django.contrib import admin

from updates.views import update_model_detail_view, JsonCBV, JsonCBV2

urlpatterns = [
    url(r'^$', update_model_detail_view),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
    url(r'^admin/', admin.site.urls),
]
