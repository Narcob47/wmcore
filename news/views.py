from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Newsletter
from .serializers import NewsletterSerializer

class NewsletterViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Newsletter.objects.all()
        serializer = NewsletterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        newsletter = get_object_or_404(Newsletter, pk=pk)
        serializer = NewsletterSerializer(newsletter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        newsletter = get_object_or_404(Newsletter, pk=pk)
        newsletter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
