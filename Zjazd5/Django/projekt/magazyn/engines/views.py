from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from engines.models import Engine

# def engine_list(request):
#     engine = Engine.objects.all()
#     return HttpResponse(engine)