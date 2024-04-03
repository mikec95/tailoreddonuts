from django.db import models


class Category(models.Model):
    """
    Represents a category for products in the ecommerce system.
    """
    # The name of the category
    name = models.CharField(max_length=255, unique=True,
                            help_text="Name of the category")

    # Optional description for the category
    description = models.TextField(
        blank=True, help_text="Description of the category")

    # A slug for the category URL
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="Unique slug for URL",)

    class Meta:
        # Display name for the model in plural form
        verbose_name_plural = 'categories'

    def __str__(self):
        # String representation of the category (its name)
        return self.name


class Product(models.Model):
    """
    Represents a product in the ecommerce system.
    """
    # Category
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True)

    # Title of the product
    item_title = models.CharField(
        max_length=250, help_text="Title of the product")

    # Price of the product
    half_dozen_price = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00, help_text="Price per half dozen")

    # Price of the product
    dozen_price = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00, help_text="Price per dozen")

    # Description of the product
    description = models.TextField(
        default="", blank=True, help_text="Description of the product")

    # Image of the product
    image = models.ImageField(upload_to='images/')

    # A slug for the product URL
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="Unique slug for URL")

    class Meta:
        # Display name for the model in plural form
        verbose_name_plural = 'products'

    def __str__(self):
        # String representation of the product (its title)
        return self.item_title
