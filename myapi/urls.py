from django.conf.urls import url, include
from django.contrib import admin

from updates.views import (
    update_model_detail_view,
    JsonCBV,
    JsonCBV2,
    SerializedListView,
    SerializedDetailView

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
]
