"""
URL configuration for uav_rental_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from uav_rental_project import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('brands/', views.brand_list_page, name='brand_list_page'),
    path('brands-page/', views.brand_detail_page, name='brand_detail_page'),
    path('brands-page/<int:id>/', views.brand_detail_page, name='brand_detail_page'),

    path('categories/', views.category_list_page, name='category_list_page'),
    path('categories-page/', views.category_detail_page, name='category_detail_page'),
    path('categories-page/<int:id>/', views.category_detail_page, name='category_detail_page'),

    path('uavs/', views.uav_list_page, name='uav_list_page'),
    path('uavs-page/', views.uav_detail_page, name='uav_detail_page'),
    path('uavs-page/<int:id>/', views.uav_detail_page, name='uav_detail_page'),

    path('rentals/', views.rental_list_page, name='rental_list_page'),
    path('rentals-page/', views.rental_detail_page, name='rental_detail_page'),
    path('rentals-page/<int:id>/', views.rental_detail_page, name='rental_detail_page'),

    path('api/', include('rentals.urls')),

    path('admin/', admin.site.urls),

]
