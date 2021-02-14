from django.db import models
from django.contrib.auth.models import User
class b_artical(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.ForeignKey(User)
