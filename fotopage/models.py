from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.utils import timezone


# Create your models here.
class About(models.Model):
    aboutme = models.CharField(max_length = 10000)
    
    def __str__(self):
        return self.aboutme

class Album(models.Model):
    title = models.CharField(max_length = 200)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(1140, 750)], 
                                format='JPEG', options={'quality': 60})
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title
    
class Lightbox(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], 
                                format='JPEG', options={'quality': 100})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(200)], 
                                format='JPEG', options={'quality': 70}, default='')
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default='Photo_Ksenia_Sheen')
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, editable=False, default='')
    
class Priceofwork(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 5000)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
class Specialoffers(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 5000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    