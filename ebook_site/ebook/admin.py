from django.contrib import admin
from .models import EBook , Author, Subject


class EBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'subject', 'ebook_category')
    list_display_links = ('id', 'title')
    list_filter = ('subject', 'authors')
    search_fields = ('title', 'description')
    list_per_page = 25


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25
  

admin.site.register(EBook, EBookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Subject, SubjectAdmin)