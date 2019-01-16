import json
from django.views.generic import View
from django.http import HttpResponse

from ..forms import UpdateModelForm
from ..models import Update as UpdateModel
from .mixins import CSRFExemptMixin
from myapi.mixins import HttpResponseMixin


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


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    List & CreateAPI view
    """

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowd"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You can not delete an entire list"})
        return HttpResponse(data, content_type="application/json")
