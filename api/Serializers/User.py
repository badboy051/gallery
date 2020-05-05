from django.contrib.auth.models import User
from rest_framework import serializers as s


class Register(s.ModelSerializer):
    password = s.CharField(max_length="50", write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(validated_data.pop("username"), is_staff=True, **validated_data)
