from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import home

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('inquiry/', include('inquiry.urls', namespace='inquiry')),
    path('menu/', include('menu.urls', namespace='menu'))
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
