from api.models import Albums
from rest_framework import serializers as s


class AlbumSerializer(s.ModelSerializer):
    pictures = s.SerializerMethodField(read_only=True, method_name="get_images")

    class META:
        model = Albums
        fields = ["id", "name", "pictures"]
        read_only_fields = ['id']

    def get_images(self, obj) -> list:
        images: list = obj.pictures_set.all()[:4].values_list("img", flat=True)
        return images;
