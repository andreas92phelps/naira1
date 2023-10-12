from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.


class User(AbstractUser):
    
    email = models.EmailField(unique=True)
   
    active = models.BooleanField(default=True)
    # photo = models.ImageField(upload_to='profile')# this solely accepts image
   #photo or whatever = models.FileField() # this accepts any file type. image, audio, video, pdf e.t.c
    date = models.DateTimeField(auto_now_add=True) # there is also 'TimeField()' and 'DateField()'. 'auto_now_add=True'assigns ONLY ONE date and time at moment of first ever login or whatever
    last_login = models.DateTimeField(auto_now=True) # 'auto_now=True'this assigns a new date and time each time the user logs in
    
    phone = models.CharField(max_length=20)
    

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



