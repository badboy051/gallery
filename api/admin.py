from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Albums.objects.all()
        else:
            return Albums.objects.filter(author=request.user)

    def get_field_queryset(self, db, db_field, request):
        return User.objects.filter(id=request.user.id)


@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ("title", "id")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Pictures.objects.all()
        else:
            return Pictures.objects.filter(album_id__author=request.user)

    def get_field_queryset(self, db, db_field, request):
        return Albums.objects.filter(author=request.user)
