from models import Books, Authors, Tags
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('name_book', 'description', 'ISBN', 'publishing_house', 'year', 'quantity')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authors
        fields = ('name',)


class TagsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('tag_name',)
