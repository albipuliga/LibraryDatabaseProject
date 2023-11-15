from django.contrib import admin
from .models import Loan, Borrower, Book, Author

# Register your models here.
admin.site.register(Loan)
admin.site.register(Borrower)
admin.site.register(Book)
admin.site.register(Author)
