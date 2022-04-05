from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


admin.site.register(Book, BookAdmin)
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


admin.site.register(Book, BookAdmin)
