import json
# from django.shortcuts import reverse
from django.views.generic import View
from ..forms import UpdateModelForm
from ..models import Update as UpdateModel
from .mixins import CSRFExemptMixin
from myapi.mixins import HttpResponseMixin
from .utils import is_json


class UpdateModeDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    Retrieve, Update & Delete view
    """
    is_json = True

    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count():
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update Not Found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(data=json_data)

    def post(self, request, id, *args, **kwargs):
        json_data = json.dumps({"message": "Not allowed, kindly use /api/updates/ endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            errot_data = json.dumps({"message": "Invalid data, sent, please send using JSON"})
            return self.get_object(id)
        obj = self.get_object(id)
        if obj is None:
            errot_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(errot_data, status=404)
        passed_data = json.loads(request.body)
        form = UpdateModelForm(passed_data)
        if form.is_valid():
            obj = form.save()
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message": "something went wrong"})
        return self.render_to_response(json_data)


    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = json.dumps({"message": "Something"})
        return self.render_to_response(json_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    List & CreateAPI view
    """
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data, status=200)

    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send json"})
            return self.render_to_response(data=error_data, status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You can not delete an entire list"})
        return self.render_to_response(data, status=403)
