from .views import home_page
from django.urls import path, include


urlpatterns = [
    path('', home_page, name='home'),
    
]