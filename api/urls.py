from django.urls import path
from store.views import CategoryViewSet, BookViewSet, TrainingViewSet, AudiobookViewSet
from news.views import NewsletterViewSet

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
    
    path('books/<int:pk>/download/', BookViewSet.as_view({
        'get': 'download'
    })),
    
    path('trainings/', TrainingViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('trainings/<int:pk>/', TrainingViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    
    path('audiobooks/', AudiobookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('audiobooks/<int:pk>/', AudiobookViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]