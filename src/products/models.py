from django.conf import settings
from django.db import models


# Django Models Unleashed 
# cfe.sh/projects/django-models-unleashed-2021

# Create your models here.

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    def get_edit_url(self):
        return f"/my-products/{self.slug}/"

    def get_delete_url(self):
        return f"/my-products/{self.slug}/delete/"

# DjangoFlix - Learn Proxy Model
# cfe.sh/projects/djangoflix

class DigitalProduct(Product):
    class Meta:
        proxy = True