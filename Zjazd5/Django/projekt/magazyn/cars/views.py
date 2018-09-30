from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car
# Create your views here.

def cars_list(request):
    cars = Car.objects.all()
    return render(
        request=request,
        context={'cars': cars},
        template_name="cars_list.html"
    )
        #HttpResponse(cars)