from django.urls import path
from news.views import NewsletterViewSet

from store.views import CategoryViewSet, BookViewSet

urlpatterns = [
    
    path('news/', NewsletterViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
        
    path('news/<int:pk>/', NewsletterViewSet.as_view({
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    
    path('categories/', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('categories/<int:pk>/', CategoryViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    
    path('books/', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('books/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]