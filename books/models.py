# from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=50)


class Tags(models.Model):
    tag_name = models.CharField(max_length=30)


class Books(models.Model):
    name_book = models.CharField(max_length=60)
    authors = models.ManyToManyField(Authors)
    tags = models.ManyToManyField(Tags)
    description = models.TextField(blank="true")
    ISBN = models.CharField(max_length=20, blank="true")
    publishing_house = models.CharField(max_length=20, blank="true")
    year = models.IntegerField(blank="true")
    quantity = models.IntegerField(blank="true")





