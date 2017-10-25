from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    created_date = models.DateField(default=date.today)
    text = RichTextField()

    def __str__(self):
        return self.Title
