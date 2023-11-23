from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255, default="")
    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=255, default="")
    publishers = models.CharField(max_length=255, default="")
    number_of_pages = models.IntegerField(default=0)
    languages = models.CharField(max_length=255, default="")

    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return self.title
