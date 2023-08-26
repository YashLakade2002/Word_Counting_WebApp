from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    words = models.IntegerField()
    charcnt = models.IntegerField()
    wspace = models.IntegerField()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title


