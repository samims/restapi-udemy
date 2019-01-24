from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from myapi.mixins import JsonResponseMixin
from .models import Update


def update_model_detail_view(request):
    data = {
        "count": 100,
        "content": "Some new content",
    }
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request):
        data = {
            "count": 100,
            "content": "Some new content"
        }

        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content",
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.serialize()
        json_data = qs
        return HttpResponse(json_data, content_type="application/json")
