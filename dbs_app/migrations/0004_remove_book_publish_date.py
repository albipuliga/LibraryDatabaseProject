# Generated by Django 4.2.7 on 2023-11-23 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dbs_app", "0003_remove_loan_book_remove_loan_borrower_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="publish_date",
        ),
    ]
