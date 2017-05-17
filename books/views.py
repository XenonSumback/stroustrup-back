# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from models import Books, Authors, Tags, Comments
from rest_framework import viewsets
from serializers import BookSerializer, AuthorSerializer, TagsSerializer, CommentSerializer


class BookList(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    # def list(self, request):
    #     queryset = Books.objects.all()
    #     serializer = BookSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def create(self, request, format=None):
    #     serializer = BookSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Books.objects.all()
    #     book = get_object_or_404(queryset, pk=pk)
    #     serializer = BookSerializer(book, context={'request': request})
    #     return Response(serializer.data)
    #
    # def update(self, request, pk = None):
    #     queryset = Books.objects.all()
    #     book = get_object_or_404(queryset, pk=pk)
    #     serializer = BookSerializer(book, data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def destroy(self, request, pk=None):
    #     queryset = Books.objects.all()
    #     book = get_object_or_404(queryset, pk=pk)
    #     book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class CommentViewSet(viewsets.ViewSet):
    queryset = Comments.objects.all()
    related = Books.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, book_id):
        queryset = Comments.objects.all()
        comments = queryset.filter(id_book=book_id)
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, book_id, format=None):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, book_id, pk=None):
        queryset = Comments.objects.all()
        comments = queryset.filter(id_book=book_id)
        comment = get_object_or_404(comments, pk=pk)
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def update(self, request, book_id, pk=None):
        queryset = Comments.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        if comment.id_user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, book_id, pk=None):
        queryset = Comments.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        if comment.id_user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def likes_handler(request, book_id):
    book = Books.objects.get(id=book_id)
    if book.likes.filter(pk=request.user.pk).exists():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return Response()



