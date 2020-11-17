from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    #* ForeignKey() field is used to create a many-to-one relationship between models.
    # on_delete:  If the author of post is deleted the post will be deleted too
    author = models.ForeignKey(User, on_delete=models.CASCADE)