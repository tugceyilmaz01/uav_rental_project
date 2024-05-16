import uuid

from django.contrib.auth.models import User
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def brand_list_page(request):
    return render(request, 'brand_list.html')


def brand_detail_page(request):
    return render(request, 'brand_detail.html')


def category_list_page(request):
    return render(request, 'category_list.html')


def category_detail_page(request):
    return render(request, 'category_detail.html')


def uav_list_page(request):
    return render(request, 'uav_list.html')


def uav_detail_page(request):
    return render(request, 'uav_detail.html')


def rental_list_page(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'rental_list.html', context)


def rental_detail_page(request):
    context = {
        'users': User.objects.all()
    }

    return render(request, 'rental_detail.html', context)
