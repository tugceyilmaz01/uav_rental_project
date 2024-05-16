from rest_framework import serializers

from rentals.models import Category, Brand, UAV, Rental


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'


class UAVListingSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = UAV
        fields = ('id', 'category', 'brand', 'model', 'weight', 'is_active')


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class RentalListingSerializer(serializers.ModelSerializer):
    uav = serializers.CharField(source='uav.model', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Rental
        fields = ('id', 'uav', 'user', 'rental_start_date', 'rental_end_date', 'is_active')
