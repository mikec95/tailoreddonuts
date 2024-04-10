from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import store

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('contact/', include('contact.urls', namespace='contact'))
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
