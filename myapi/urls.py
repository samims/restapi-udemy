from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
    url(r'^api/auth/', include('accounts.api.urls')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/books/', include('books.api.urls')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
]
