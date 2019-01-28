from rest_framework.generics import ListAPIView, CreateAPIView
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


class StatusAPIView(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()



class StatusDetailAPIView:
    pass


class StatusUpdateAPIView:
    pass


class StatusDeleteAPIView:
    pass
