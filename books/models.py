# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.tag_name


class Book(models.Model):
    name_book = models.CharField(max_length=60)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(blank=True)
    ISBN = models.CharField(max_length=20, blank=True)
    publishing_house = models.CharField(max_length=20, blank=True)
    year = models.IntegerField(blank=True)
    quantity = models.IntegerField(blank=True)
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name_book


class Comment(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    date = models.DateField()
    comment = models.TextField()

    def __unicode__(self):
        return self.id_book
