from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Represents a category for products in the ecommerce system.
    """
    name = models.CharField(max_length=255, unique=True,
                            help_text="Name of the category")
    description = models.TextField(
        blank=True, help_text="Description of the category")
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="Unique slug for URL")

    class Meta:
        verbose_name_plural = 'categories'  # Display name for the model in plural form

    def __str__(self):
        return self.name  # String representation of the category (its name)

    def get_absolute_url(self):
        # Return the absolute URL for the category
        return reverse("list-category", args={self.slug})


class Product(models.Model):
    """
    Represents a product in the ecommerce system.
    """
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True)
    item_title = models.CharField(
        max_length=250, help_text="Title of the product")
    half_dozen_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00,
                                           help_text="Price per half dozen")
    dozen_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00,
                                      help_text="Price per dozen")
    description = models.TextField(
        default="", blank=True, help_text="Description of the product")
    image = models.ImageField(
        upload_to='images/', default='images/default-image.png')
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="Unique slug for URL")

    class Meta:
        verbose_name_plural = 'products'  # Display name for the model in plural form

    def __str__(self):
        # String representation of the product (its title)
        return self.item_title

    def get_absolute_url(self):
        # Return the absolute URL for the product
        return reverse("product-info", args={self.slug})
