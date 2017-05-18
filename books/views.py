# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from models import Book, Author, Tag, Comment
from rest_framework import viewsets
from serializers import BookSerializer, AuthorSerializer, TagsSerializer, CommentSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class CommentViewSet(viewsets.ViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    serializer_class = CommentSerializer

    def list(self, request, book_id):
        comments = Comment.objects.filter(book=book_id)
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, book_id=None):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, book_id, pk=None):
        comment = get_object_or_404(Comment, book=book_id, pk=pk)
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def update(self, request, book_id, pk=None):
        comment = get_object_or_404(Comment, pk=pk, book=book_id)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, book_id=None, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def likes_handler(request, book_id):
    """
    API endpoint that allows to add and delete likes.
    """
    book = Book.objects.get(id=book_id)
    if book.likes.filter(pk=request.user.pk).exists():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return Response()
