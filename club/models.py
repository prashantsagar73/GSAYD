from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=2000)
    content2 = models.TextField(max_length=5000)
    date_time= models.DateField(default = timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("clubs_detail", kwargs={'pk': self.pk})