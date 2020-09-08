from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

handler404 = 'myapp.views.custom_404' #new 
