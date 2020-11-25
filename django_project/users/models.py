from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    #! OneToOneField ----> means that one user can only have one profile, and viseversa!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")