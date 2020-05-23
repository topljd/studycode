from django.db import models
from django.core import validators
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #thumnail = models.FileField()
    # thumnail = models.FileField(upload_to='%Y/%m/%d/',validators=[validators.FileExtensionValidator(['txt'],message='thumbnial')])
    thumbnail = models.ImageField(upload_to='%Y/%m/%d/')

