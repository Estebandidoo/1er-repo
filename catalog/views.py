from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    num_Books = Book.objects.all().count()
    num_Instances = BookInstance.objects.all().count()

    num_Instances_available = BookInstance.objects.filter(status__exact='a').count()  
    num_Authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_Books':num_Books,'num_Instances':num_Instances,'num_Instances_available':num_Instances_available,'num_Authors':num_Authors},
    )





# Create your views here.
