from models import Book, Author, Tag, Comment
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name_book', 'authors', 'tags', 'description', 'ISBN', 'publishing_house',
                  'year', 'quantity', 'likes')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)


class TagsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'date', 'comment')
