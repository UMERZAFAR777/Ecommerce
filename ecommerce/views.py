from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Slider,Banner


def base(request):
    return render (request,'base.html')


def home (request):
    sliders = Slider.objects.all()
    banners = Banner.objects.all()
   
    context = {
        'sliders':sliders,
        'banners':banners,
    }
    return render (request,'home.html',context)





