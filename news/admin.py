from django.contrib import admin

from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading', 'published_date', 'author')
    search_fields = ('title', 'heading', 'content', 'author')
    list_filter = ('published_date', 'author')
