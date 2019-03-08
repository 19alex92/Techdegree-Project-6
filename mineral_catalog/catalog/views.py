from django.shortcuts import render
from django.http import HttpResponse


def mineral_list(request):
    return render(request, 'catalog/mineral_list.html')


def mineral_detail(request):
    return render(request, 'catalog/mineral_detail.html')