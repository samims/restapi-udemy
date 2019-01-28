from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


# CreateModelMixin & UpdateModelMixin for post & put data
class StatusAPIView(CreateModelMixin, ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusUpdateAPIView(UpdateAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    # lookup_field = 'id'


class StatusDeleteAPIView(DestroyAPIView):
    # authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
