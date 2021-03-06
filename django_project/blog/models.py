from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    #* ForeignKey() field is used to create a many-to-one relationship between models.
    #* One to Many: in this case it means we can have one author and many posts but one post can only have one author
    # on_delete:  If the author of post is deleted the post will be deleted too
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Print out title in shell for database queries or sth like this
    def __str__(self):
        return self.title
        
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})