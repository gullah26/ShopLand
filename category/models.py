from django.db import models


# Create your models here.
# custom category model

class Category(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to='photos/categories',
                                       blank=True)
    description = models.TextField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
