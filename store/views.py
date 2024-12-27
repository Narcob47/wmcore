from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.http import FileResponse
from .models import Category, Book, Training, Audiobook
from .serializers import CategorySerializer, BookSerializer, TrainingSerializer, AudiobookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']  # Add fields you want to filter by
    search_fields = ['title']  # Add fields you want to search by
    ordering_fields = ['title']  # Add fields you want to order by

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'category']  # Add fields you want to filter by
    search_fields = ['title', 'author']  # Add fields you want to search by
    ordering_fields = ['title', 'published_date']  # Add fields you want to order by

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        book = self.get_object()
        file_handle = book.file_upload.open()
        response = FileResponse(file_handle, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{book.file_upload.name}"'
        return response

class TrainingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']  # Add fields you want to filter by
    search_fields = ['title']  # Add fields you want to search by
    ordering_fields = ['title', 'date_created']  # Add fields you want to order by

class AudiobookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']  # Add fields you want to filter by
    search_fields = ['title']  # Add fields you want to search by
    ordering_fields = ['title', 'date_created']  # Add fields you want to order by
