# Create your views here.
from django.shortcuts import render


def main_page(request):
    return render(request, "ndweb/home.html",)