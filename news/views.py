from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Newsletter
from .serializers import NewsletterSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']  # Add fields you want to filter by
    search_fields = ['title']  # Add fields you want to search by
    ordering_fields = ['title']  # Add fields you want to order by

