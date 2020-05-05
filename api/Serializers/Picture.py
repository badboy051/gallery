from api.models import Pictures, Albums
from rest_framework import serializers as s
from django.shortcuts import get_object_or_404


class PictureSerializer(s.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ["id", "title", "desc", "img", "upload_date"]
        read_only_fields = ['id']

    def create(self, validated_data):
        picture = Pictures(
            album_id=get_object_or_404(Albums, name=self.context['request'].resolver_match.kwargs.get("name"),
                                       author=self.context['request'].user), **validated_data)
        picture.save()
        return picture
