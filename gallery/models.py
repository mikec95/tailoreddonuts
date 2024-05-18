from django.db import models
from django.urls import reverse
# Create your models here.


class GalleryImage(models.Model):
    """
    Represents an Image in the gallery module.
    """
    image_title = models.CharField(
        max_length=250, help_text="Image Title")
    description = models.TextField(
        default="", blank=True, help_text="Description of the product")
    image = models.ImageField(
        upload_to='gallery/images', default='images/default-image.png')

    class Meta:
        # Display name for the model in plural form
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        # String representation of the product (its title)
        return self.image_title

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
