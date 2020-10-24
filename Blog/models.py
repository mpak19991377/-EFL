from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    Title = models.CharField(max_length=50)
    Slug = models.CharField(max_length=50, unique=True)
    Position = models.IntegerField(unique=True)
    Published = models.DateField(default=timezone.now)
    Status = models.BooleanField(default=True, verbose_name='To Be Published ?')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = [
            'Position',
        ]
    def __str__(self):
        return self.Title    



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
    Category = models.ManyToManyField(Category)
    Published = models.DateField(default=timezone.now)
    Status = models.CharField(max_length=1, choices=Status_Choices, default='P')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'

    def __str__(self):
        return self.Title   



