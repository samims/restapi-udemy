import json
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
            error_data = json.dumps({"message": "Invalid data sent, send json"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=400)
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({"mesage": "Something"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        deleted_, _ = obj.delete()
        if deleted_:
            json_data = json.dumps({"message": "Deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({"mesage": "Could not delete item, Please try again"})
        return self.render_to_response(error_data, status=400)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    single endpoint for CRUD
    """
    is_json = True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        data = {}
        if request.body:
            is_valid = is_json(request.body)
            if not is_valid:
                data = json.dumps({"message": "Please send Json Data"})
                return self.render_to_response(data=data, status=400)
            data = json.loads(request.body)
        passed_id = data.get('id')
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"message": "Object not found"})
                return self.render_to_response(error_data, status=400)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        qs = self.get_queryset()
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

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, send json"})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id')
        if not passed_id:
            error_data = json.dumps({"id": "This is a required field to update an item"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_data, status=400)
        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({"mesage": "Something"})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({"id": "This is a required field to update an item"})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_data, status=400)

        deleted_, _ = obj.delete()
        if deleted_:
            json_data = json.dumps({"message": "Successfully deleted."})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({"message": "Could not delete item, please try again"})
        return self.render_to_response(error_data, status=400)
