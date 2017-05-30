from django.contrib.auth.models import User

from models import Book, Author, Tag, Comment
from users.serializers import UserSerializer
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)


class TagsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name',)


class BookSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.IntegerField(source='likes.count', read_only=True)
    authors = AuthorSerializer(many=True)
    tags = TagsSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name_book', 'authors', 'tags', 'description', 'ISBN', 'publishing_house',
                  'year', 'quantity', 'likes')
        depth = 2


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) # user = UserField(default=CurrentUser)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'date', 'comment')
        # read_only_fields = ()
