from django.contrib import admin

from gallery.models import GalleryImage

# Register your models here.


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'description', 'image', 'slug')
    search_fields = ('image_title', 'description', 'slug')
