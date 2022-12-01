from django.contrib import admin
from django.urls import path, include
from xia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top, name = 'top'),
]