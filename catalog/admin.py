from django.contrib import admin

from . models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

# Register your models here.
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver

#git init
#git config --global user.name "" o --global user.mail ""
#git status
#git add --all
#git comit 