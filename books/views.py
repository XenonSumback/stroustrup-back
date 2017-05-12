from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from models import Books, Authors, Tags
from rest_framework import viewsets
from serializers import BookSerializer, AuthorSerializer, TagsSerializer


class BookViewSet(viewsets.ViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
