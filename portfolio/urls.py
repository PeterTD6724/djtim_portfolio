from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path("admin/", admin.site.urls),
    path("thepdt/", admin.site.urls),
    path("", include("main.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
