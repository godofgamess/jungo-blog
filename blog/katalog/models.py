from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=True, default='')
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.SET_NULL)
    foto = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name