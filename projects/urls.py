from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('project.urls'), name='projects'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('register/', views.register, name='register'),
    path('', include('general.urls'), name='general')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
