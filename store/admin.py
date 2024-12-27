from django.contrib import admin
from .models import Category, Book, Training, Audiobook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    search_fields = ('title', 'category__title')
    list_filter = ('category',)

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_created', 'date_updated')
    search_fields = ('title', 'slug')
    list_filter = ('date_created', 'date_updated')

@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_created', 'date_updated')
    search_fields = ('title', 'slug')
    list_filter = ('date_created', 'date_updated')
