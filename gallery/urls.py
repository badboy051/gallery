"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from api.Views import PictureList,PictureView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("album/<str:name>/pictures", PictureList.as_view()),
                  re_path(r"^picture/(?P<id>[0-9 abcdef]{8})/?$", PictureView.as_view()),
              ]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
