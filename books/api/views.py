import json

from django.views import View

from myapi.mixins import HttpResponseMixin

from ..forms import BookModelForm
from ..models import Book as BookModel
from .mixins import CSRFExemptMixin
from .utils import is_json


class BookListCreateAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True
    queryset = None

    def get_queryset(self):
        qs = BookModel.objects.all()
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
            data = json.loads(request.body)
        passed_id = data.get('id')
        if passed_id:
            obj = self.get_object(id=passed_id)
            if not obj:
                data = json.dumps({"message": "Object not found"})
                return self.render_to_response(data, status=404)
            data = obj.serialize()
            return self.render_to_response(data, status=200)
        data = BookModel.objects.all()
        json_data = data.serialize()
        return self.render_to_response(data=json_data, status=200)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = BookModelForm(data)
        if form.is_valid():
            form.save()
            data = json.dumps({"message": "Object created"})
            return self.render_to_response(data, status=200)
        elif form.errors:
            return self.render_to_response(json.dumps(form.errors), status=400)
        data = json.dumps({"message": "Something went wrong"})
        return self.render_to_response(data, status=500)

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            data = json.dumps({"message": "Kindly send json"})
            return self.render_to_response(data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get("id")
        if not passed_id:
            return self.render_to_response(json.dumps({"id": "This field is require"}))
        obj = self.get_object(id=passed_id)
        if not obj:
            data = json.dumps({"message": "Object not found."})
            return json.dumps(data, status=404)

        data = json.loads(obj.serialize())
        for k, v in passed_data.items():
            data[k] = v
        form = BookModelForm(data, instance=obj)
        if form.is_valid():
            form.save()
            data = json.dumps({"message": "Updated"})
            return self.render_to_response(data, status=200)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        return self.render_to_response(json.dumps({"message": "Something"}))

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            data = json.dumps({"message": "Please send valid json"})
            return self.render_to_response(data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id')
        if not passed_id:
            return self.render_to_response(json.dumps({"id": "this field is required"}), status=400)
        obj = self.get_object(id=passed_id)
        if not obj:
            return self.render_to_response(json.dumps({"message": "Object not found"}), status=400)
        deleted_, _ = obj.delete()
        if deleted_:
            return self.render_to_response(json.dumps({"message": "Successfully deleted"}), status=200)
        return self.render_to_response(json.dumps({"message": "Something went wrong"}), status=500)
