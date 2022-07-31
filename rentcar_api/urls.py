from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('company_app.urls')),
    path('', include('services_app.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
