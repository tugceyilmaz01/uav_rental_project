from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rentals.filters import CategoryFilter, BrandFilter, UAVFilter, RentalFilter
from rentals.models import Category, Brand, UAV, Rental
from rentals.serializers import CategorySerializer, BrandSerializer, UAVListingSerializer, UAVSerializer, \
    RentalSerializer, RentalListingSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('-id')
    serializer_class = BrandSerializer
    filterset_class = BrandFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter


class UAVViewSet(viewsets.ModelViewSet):
    queryset = UAV.objects.all().order_by('-id')
    serializer_class = UAVSerializer
    filterset_class = UAVFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return UAVListingSerializer

        return super().get_serializer_class()


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all().order_by('-id')
    serializer_class = RentalSerializer
    filterset_class = RentalFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return RentalListingSerializer

        return super().get_serializer_class()
