"""Directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from teachers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('import/', views.teacher_import, name='teacher_import'),
    # Add URL patterns for AJAX filtering here
    path('filter/last_name/<str:letter>/', views.filter_by_last_name, name='filter_by_last_name'),
    path('filter/subject/<str:subject>/', views.filter_by_subject, name='filter_by_subject'),
]



