# from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
    name_book = models.CharField(max_length=60),
    description = models.TextField(blank="true"),
    ISBN = models.CharField(max_length=20, blank="true"),
    publishing_house = models.CharField(max_length=20, blank="true"),
    year = models.IntegerField(blank="true"),
    quantity = models.IntegerField(blank="true")


class Authors(models.Model):
    name = models.CharField(max_length=50),


class Tags(models.Model):
    tag_name = models.CharField(max_length=30),


class BooksAuthors(models.Model):
    id_book = models.ForeignKey(Books),
    id_author = models.ForeignKey(Authors),


class BooksTags(models.Model):
    id_book = models.ForeignKey(Books),
    id_tag = models.ForeignKey(Tags)

