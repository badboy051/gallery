from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
def lam():
    return str(uuid4())[:8]
class albums(models.Model):
    name=models.CharField(max_length=100)
    creation_date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
class picturs(models.Model):
    id=models.CharField(primary_key=True,default=lam,unique=True,editable=False,max_length=8)
    album_id=models.ForeignKey(albums,null=True,on_delete=models.SET_NULL,blank=True)
    title=models.CharField(max_length=100)
    desc=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='images/',null=True)
    upload_date=models.DateTimeField(auto_now_add=True)




