from models import Books, Authors, Tags
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name_book', 'authors', 'tags', 'description', 'ISBN', 'publishing_house', 'year', 'quantity')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'name',)


class TagsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'tag_name',)
