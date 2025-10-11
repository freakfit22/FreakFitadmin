from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from freakfitapp.views import homepage_view  # 👈 update import

urlpatterns = [
    path('', homepage_view, name='home'),
    path('admin/', admin.site.urls),
    path('freakfitapp/', include('freakfitapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
