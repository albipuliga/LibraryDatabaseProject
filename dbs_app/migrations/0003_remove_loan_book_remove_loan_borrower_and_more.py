# Generated by Django 4.2.7 on 2023-11-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbs_app", "0002_author_book_borrower_loan_delete_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loan",
            name="book",
        ),
        migrations.RemoveField(
            model_name="loan",
            name="borrower",
        ),
        migrations.RemoveField(
            model_name="author",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="book",
            name="price",
        ),
        migrations.AddField(
            model_name="author",
            name="key",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="book",
            name="languages",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="book",
            name="number_of_pages",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="book",
            name="publish_date",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="book",
            name="publishers",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.DeleteModel(
            name="Borrower",
        ),
        migrations.DeleteModel(
            name="Loan",
        ),
    ]
