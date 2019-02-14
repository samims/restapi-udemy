from django.conf.urls import url

from .views import BookListCreateAPIView

urlpatterns = [
    url(r'^$', BookListCreateAPIView.as_view()),

]
