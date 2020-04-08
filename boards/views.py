from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

# Create your views here.
from boards.forms import NewTopicForm
from boards.models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def hello(request):
    return render(request, 'boards/hello.html')


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})

