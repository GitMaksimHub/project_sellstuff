from django.db import models
from django.urls import reverse


#python manage.py makemigrations
#python manage.py sqlmigrate main_app 0001
#python manage.py migrate


#comment dlya Ilii

class db_test(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('test_path', kwargs={"slug_id":self.slug})


class db_api_test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)