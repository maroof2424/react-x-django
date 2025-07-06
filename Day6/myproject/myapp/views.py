from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here.

def orm_view(request):
    return HttpResponse("Orm")