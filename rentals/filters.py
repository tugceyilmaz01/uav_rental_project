import django_filters


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(lookup_expr='exact')


class BrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(lookup_expr='exact')


class UAVFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(lookup_expr='exact')
    brand = django_filters.NumberFilter(lookup_expr='exact')
    model = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(lookup_expr='exact')


class RentalFilter(django_filters.FilterSet):
    uav = django_filters.NumberFilter(lookup_expr='exact')
    user = django_filters.NumberFilter(lookup_expr='exact')
