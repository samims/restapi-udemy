import json
from django.views.generic import View
from django.http import HttpResponse
from ..models import Update as UpdateModel
from .mixins import CSRFExemptMixin


class UpdateModeDetailAPIView(CSRFExemptMixin, View):
    """
    Retrieve, Update & Delete view
    """

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")


class UpdateModelListAPIView(CSRFExemptMixin, View):
    """
    List & CreateAPI view
    """

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "Unknown data"})
        return HttpResponse(data, content_type="application/json")

    def delete(self, reqiest, *args, **kwargs):
        data = json.dumps({"message": "You can not delete an entire list"})
        return HttpResponse(data, content_type="application/json")
