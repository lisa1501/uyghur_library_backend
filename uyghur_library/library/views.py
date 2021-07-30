from django.shortcuts import render
from .models import Book
# from django.http import HttpResponse


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})