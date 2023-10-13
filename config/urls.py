from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('public.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.site_header = "SuperAdmin isTech"
admin.site.site_title = "isTech"
admin.site.index_title = "Admin"