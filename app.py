import streamlit as st
import django
import os

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbs.settings")
django.setup()

from dbs_app.models import Book, Author

# Streamlit app
st.title("Library Database")


# Function to search books
def search_books(query):
    books = Book.objects.filter(title__icontains=query)
    return books


def search_isbn(query):
    isbn = Book.objects.filter(isbn__icontains=query)
    return isbn


def search_authors(query):
    authors = Author.objects.filter(name__icontains=query)
    return authors


def search_author_by_key(query):
    author_by_key = Author.objects.filter(key__icontains=query)
    return author_by_key


def search_publishers(query):
    publishers = Book.objects.filter(publishers__icontains=query)
    return publishers


# User input
search_query = st.text_input("Enter a book title, author name, or publisher to search:")

# Button to perform search
if st.button("Search"):
    if search_query:
        # Perform search
        result_books = search_books(search_query)
        result_isbn = search_isbn(search_query)
        result_authors = search_authors(search_query)
        result_author_by_key = search_author_by_key(search_query)
        result_publishers = search_publishers(search_query)

        # Display results
        if result_books.exists():
            for book in result_books:
                st.write(f"TITLE: {book.title}")
                st.write(f"AUTHOR: {book.author.name}")
                st.write(f"PUBLISHER: {book.publishers}")
                st.write(f"NUMBER OF PAGES: {book.number_of_pages}")
                st.write(f"ISBN: {book.isbn}")
                st.write("---")
        elif result_authors.exists():
            for author in result_authors:
                st.write(f"KEY: {author.key}")
                st.write("Books written by this author:")
                st.write("---")
                # Display books written by the author
                books_by_author = Book.objects.filter(author=author)
                if books_by_author.exists():
                    for book in books_by_author:
                        st.write(f"TITLE: {book.title}")
                        st.write(f"PUBLISHER: {book.publishers}")
                        st.write(f"NUMBER OF PAGES: {book.number_of_pages}")
                        st.write(f"ISBN: {book.isbn}")
                        st.write("---")
                else:
                    st.write("No books found for this author.")
        elif result_author_by_key.exists():
            for author in result_author_by_key:
                st.write(f"NAME: {author.name}")
                st.write("Books written by this author:")
                st.write("---")
                # Display books written by the author
                books_by_author = Book.objects.filter(author=author)
                if books_by_author.exists():
                    for book in books_by_author:
                        st.write(f"TITLE: {book.title}")
                        st.write(f"PUBLISHER: {book.publishers}")
                        st.write(f"NUMBER OF PAGES: {book.number_of_pages}")
                        st.write(f"ISBN: {book.isbn}")
                        st.write("---")
                else:
                    st.write("No books found for this author.")
        elif result_publishers.exists():
            for publisher in result_publishers:
                st.write(f"TITLE: {publisher.title}")
                st.write(f"AUTHOR: {publisher.author.name}")
                st.write(f"PUBLISHER: {publisher.publishers}")
                st.write(f"NUMBER OF PAGES: {publisher.number_of_pages}")
                st.write(f"ISBN: {publisher.isbn}")
                st.write("---")
        elif result_isbn.exists():
            for isbn in result_isbn:
                st.write(f"TITLE: {isbn.title}")
                st.write(f"AUTHOR: {isbn.author.name}")
                st.write(f"PUBLISHER: {isbn.publishers}")
                st.write(f"NUMBER OF PAGES: {isbn.number_of_pages}")
                st.write(f"ISBN: {isbn.isbn}")
                st.write("---")
                
        else:
            st.write(
                "No books, authors, or publishers found with that title, name, or publisher."
            )
    else:
        st.write("Please enter a title, name, or publisher to search.")
