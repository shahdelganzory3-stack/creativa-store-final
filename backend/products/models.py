from django.db import models
from django.db.models import Index
from django.urls import reverse
from django.conf import settings 
from django.utils.text import slugify 

class Category(models.Model):
   
    name = models.CharField(max_length=200, db_index=True, verbose_name="sections name")
   
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="(Slug)") 

    class Meta:
        ordering = ('name',)
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

  
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
   
    
    bose_name="Available colors"
        
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="department")
    name = models.CharField(max_length=200, db_index=True, verbose_name="product name")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="link sub-product") 
    image = models.URLField(max_length=500, blank=True, null=True, verbose_name="Image link")
    description = models.TextField(blank=True, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (gm)")
    available = models.BooleanField(default=True, verbose_name="Available for viewing")
    created = models.DateTimeField(auto_now_add=True, verbose_name="dateCreation"
)
    updated = models.DateTimeField(auto_now=True)
   
    available_sizes = models.CharField(
        max_length=255, 
        default='S,M,L,XL', 
        help_text="Enter sizes separated by comma (e.g., S,M,L,XL)",
        verbose_name="Available sizes"
    )
    available_colors = models.CharField(
        max_length=255, 
        default='Pink,Blue,Black', 
        help_text="Enter colors separated by comma (e.g., Pink,Blue,Black)",
        verbose_name="Available colors"
    )

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Order(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )
    name = models.CharField(max_length=150, verbose_name="custmore name ")
    phone = models.CharField(max_length=20, verbose_name="phone number")
    address = models.CharField(max_length=250, verbose_name="Shipping address")
    paid = models.BooleanField(default=False, verbose_name="Payment status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="date demand")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'customer request'
        verbose_name_plural = 'Customer requests'

    def __str__(self):
        return f'Dial a number{self.id} by {self.name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="demand")
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name="Product")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price at time of purchase")
    quantity = models.PositiveIntegerField(default=1, verbose_name="quantity")

    class Meta:
        verbose_name = 'Request item'
        verbose_name_plural = 'request items'

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity