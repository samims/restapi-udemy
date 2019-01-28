from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


class StatusAPIView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id')
        # queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(Status, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id')
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super(StatusAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
