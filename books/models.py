# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tags(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class Books(models.Model):
    name_book = models.CharField(max_length=60)
    authors = models.ManyToManyField(Authors)
    tags = models.ManyToManyField(Tags)
    description = models.TextField(blank="true")
    ISBN = models.CharField(max_length=20, blank="true")
    publishing_house = models.CharField(max_length=20, blank="true")
    year = models.IntegerField(blank="true")
    quantity = models.IntegerField(blank="true")
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.name_book


class Comments(models.Model):
    id_book = models.ForeignKey(Books)
    id_user = models.ForeignKey(User)
    date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return self.id_book







