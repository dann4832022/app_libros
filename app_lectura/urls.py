from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from .views import inicio


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('usuario/', include('apps.usuarios.ulrs')),
    path("libros/", include('apps.libros.urls')),
    path("opiniones/", include('apps.opiniones.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

