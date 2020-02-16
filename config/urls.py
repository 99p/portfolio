from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('admin/', admin.site.urls),
]
