from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
    )
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include('accounts.urls'))
]

spectacular_urlpatterns = [
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path(
       'api/docs/',
       SpectacularSwaggerView.as_view(url_name='schema'),
       name='swagger-ui'
       ),
   path(
       'api/redoc/',
       SpectacularRedocView.as_view(url_name='schema'),
       name='redoc'
       ),
]

urlpatterns = (
    urlpatterns +
    spectacular_urlpatterns +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
