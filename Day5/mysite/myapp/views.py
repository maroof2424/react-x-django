from django.shortcuts import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("Hello Django")