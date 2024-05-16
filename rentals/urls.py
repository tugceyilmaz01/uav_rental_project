from django.urls import include, path
from rest_framework import routers

from rentals import views

router = routers.DefaultRouter()
router.register(r'brands', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'uavs', views.UAVViewSet)
router.register(r'rentals', views.RentalViewSet)

urlpatterns = [
    path('', include(router.urls))
]
