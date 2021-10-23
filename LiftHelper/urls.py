from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('accounts/', include('allauth.urls')),
    path('codewars/', include('CodeWarsHelper.urls'))
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

