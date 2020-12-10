from django.db import models
import uuid
from django.utils import timezone
from django.template.defaultfilters import slugify


class Product(models.Model):
    # Model fields create products.
    name = models.CharField(max_length=50)
    sku = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField()
    image = models.CharField(max_length=150, blank=True)
    descrption = models.CharField(max_length=150, blank=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=3)
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.name)
        queryset = Product.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Product.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug
            
        if self.featured:
            try:
                temp = Product.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Product.DoesNotExist:
                pass
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
