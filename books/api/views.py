import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from books.models import Book as BookModel
from myapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from .utils import is_json


class BookListCreateAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request):
        data = BookModel.objects.all()
        json_data = data.serialize()
        return self.render_to_response(data=json_data, status=200)

    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            return self.render_to_response(data=json.dumps({"message": "Not valid data"}), status=400)
        return self.render_to_response(data=json.dumps({"message": "Valid"}), status=200)
