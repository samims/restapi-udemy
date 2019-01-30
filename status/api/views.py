import json
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = StatusSerializer
    padded_id = None

    def __init__(self):
        super(StatusAPIView, self).__init__()
        self.passed_id = None

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id') or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id')
        json_data = {}
        body_ = request.body
        print(request.body)
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id')
        passed_id = url_passed_id or new_passed_id
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super(StatusAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id')
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id')
        passed_id = url_passed_id or new_passed_id
        print(passed_id)
        self.passed_id = passed_id
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id')
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id')
        passed_id = url_passed_id or new_passed_id
        print(passed_id)
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id')
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id')
        passed_id = url_passed_id or new_passed_id
        print(passed_id)
        self.passed_id = passed_id
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id')
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id')
        passed_id = url_passed_id or new_passed_id
        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)
