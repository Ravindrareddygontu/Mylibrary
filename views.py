from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response


class BookList(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def books(request):
    book = Book.objects.all()
    return render(request, 'home.html', {'book': book})


@login_required(login_url='/loginuser')
def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('/')

    return render(request, 'addbook.html', {'form': form})


@login_required(login_url='/loginuser')
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request, 'deletebook.html', {'book': book})


@login_required(login_url='/loginuser')
def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('/')

    return render(request, 'updatebook.html', {'form': form})


def logoutuser(request):
    logout(request)
    return redirect('/')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User name not exit')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('/')
        else:
            messages.error(request, 'User or password does not exit')
    return render(request, 'login.html')


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.save()
           login(request, user)
           return redirect('/')
        else:
            messages.error(request, 'Something is done wrong')
    return render(request, 'register.html', {'form': form})

