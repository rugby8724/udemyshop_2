from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=247, unique=True)
    slug = models.SlugField(max_length=247, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:productsbycategory', kwargs={'slug':self.slug})

class Product(models.Model):
        name = models.CharField(max_length=247, unique=True)
        slug = models.SlugField(max_length=247, unique=True)
        description = models.TextField(blank=True)
        category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        image = models.ImageField(upload_to='product', blank=True)
        stock = models.IntegerField()
        available = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['name']
            verbose_name = 'product'
            verbose_name_plural = 'products'

        def __str__(self):
            return self.name

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Product, self).save(*args, **kwargs)

        def get_absolute_url(self, *args, **kwargs):
            return reverse('shop:singleproduct', kwargs={'slug':self.slug})
