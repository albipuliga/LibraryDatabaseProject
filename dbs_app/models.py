from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return self.title


class Borrower(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField()

    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return self.name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    date_returned = models.DateField(null=True, blank=True)

    # class Meta:
    #     # Set the database alias to 'mongodb'
    #     database = 'mongodb'

    def __str__(self):
        return f"{self.book} borrowed by {self.borrower}"
