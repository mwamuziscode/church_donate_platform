
from django.contrib import admin
from django.urls import path, include
# settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donations.urls'))
]


# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
#handler404 = 'donations.views.page_not_found_view'
#handler500 = 'donations.views.server_error_view


