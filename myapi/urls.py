from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/jwt/$', obtain_jwt_token),
    url(r'^api/auth/jwt/refresh/$', refresh_jwt_token),
    url(r'^api/updates/', include('updates.api.urls')),
    url(r'^api/books/', include('books.api.urls')),
    url(r'^api/status/', include('status.api.urls')),
]
