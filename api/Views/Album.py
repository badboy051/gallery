from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.Serializers import AlbumSerializer
from rest_framework.permissions import IsAuthenticated


class AlbumList(ListCreateAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = ["name"]

    def get_queryset(self):
        return self.request.user.albums_set.all()


class AlbumView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "name"

    def get_queryset(self):
        return self.request.user.albums_set.all()
