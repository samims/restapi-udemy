from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
    url(r'^api/books/', include('books.api.urls')),
    url(r'^api/status/', include('status.api.urls')),
]
