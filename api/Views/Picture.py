from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Pictures, Albums
from api.Serializers import PictureSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class PictureList(ListCreateAPIView):
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    lookup_url_kwarg = ["name"]

    def get_queryset(self):
        query = get_object_or_404(Albums, author=self.request.user, name=self.kwargs.get("name"))
        query = query.pictures_set.all()
        return query


class PictureView(RetrieveUpdateDestroyAPIView):
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Pictures.objects.filter(album_id__author=self.request.user)
