from rest_framework.generics import CreateAPIView
from api.Serializers import Register
from django.shortcuts import redirect


class Register(CreateAPIView):

    serializer_class = Register

    def get_queryset(self):
        if self.request.user is not None:
            raise redirect("docs")
        return self.request.user.albums_set.all()
