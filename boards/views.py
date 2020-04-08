from django.shortcuts import render, HttpResponse


# Create your views here.
from boards.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def hello(request):
    return render(request, 'boards/hello.html')
