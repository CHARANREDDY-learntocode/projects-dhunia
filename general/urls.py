from django.urls import path

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(template_name='general/index.html'), name='home')
]