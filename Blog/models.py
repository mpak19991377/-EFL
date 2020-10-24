from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    Status_Choices = {
        ('P', 'Published'),
        ('D', 'Draft')
    }
    Title = models.CharField(max_length=120)
    Slug = models.CharField(max_length=120, unique=True)
    Image = models.ImageField(upload_to='photo')
    descraption = models.TextField()
    Writer_Name = models.CharField(max_length=50, verbose_name='writer name :')
    Published = models.DateField(default=timezone.now)
    Status = models.CharField(max_length=1, choices=Status_Choices, default='P')



