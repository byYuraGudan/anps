from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('Hello, World!')


def hello(request):
    return render(request, 'boards/hello.html')
