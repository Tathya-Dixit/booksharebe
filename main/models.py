from django.db import models
from django.contrib.auth.models import User



class Genre(models.Model):
    name = models.CharField(max_length=255,default="")
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['images',str(instance.title),filename])
    genre = models.ForeignKey(Genre, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='')
    author = models.CharField(max_length=60,default='')
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = nameFile, blank = True, null = True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    