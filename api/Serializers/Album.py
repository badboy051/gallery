from api.models import Albums
from rest_framework import serializers as s
from django.conf import settings


class AlbumSerializer(s.ModelSerializer):
    pictures = s.SerializerMethodField(
        read_only=True, method_name="get_images")

    class Meta:
        model = Albums
        fields = ["id", "name", "pictures"]
        read_only_fields = ['id']

    def get_images(self, obj) -> list:
        images: list = obj.pictures_set.all()[:4].values_list("img", flat=True)
        return ["http://"+self.context['request'].get_host() + settings.MEDIA_URL + image for image in images]

    def create(self, validated_data):
        album = Albums(author=self.context['request'].user, **validated_data)
        album.save()
        return album
