from django.db import models
from django.conf import settings

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to="post")#the images will be uploaded to 'post' whenever a user uploads an image
    other = models.ImageField(upload_to="post",default="")
    dateCreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)#means that once the user has made a post, their account 'is_active' status will immediately become 'false'. Until the admin has evaluated the post.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)#the parameter User is to link to 'auth_user' table created by Django. This will meake it impossible for someone to post without being a registered user.
    #'on_delete=models.CASCADE' means that once the user account is deleted, all their posts will be deleted.
    #'on_delete=models.RESTRICT' menas that once the user account is deleted, all their posts will be restricted.



