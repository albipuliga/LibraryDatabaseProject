import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for book_elem in soup.find_all('tr', itemtype='http://schema.org/Book'):
        # Extracting book details
        title_elem = book_elem.find('a', class_='bookTitle')
        author_elem = book_elem.find('span', itemprop='author')
        rating_elem = book_elem.find('span', class_='minirating')
        ratings_count_elem = book_elem.find('span', class_='smallText uitext')
        published_elem = book_elem.find('div', class_='greyText smallText')
        description_elem = book_elem.find('span', style='display:none', itemprop='description')

        # Extracting additional details
        avg_rating = rating_elem.text.strip().split()[0] if rating_elem else 'N/A'
        ratings_count = ratings_count_elem.text.strip().split()[0] if ratings_count_elem else 'N/A'
        published_year = published_elem.text.strip().split()[-1] if published_elem else 'N/A'
        description = description_elem.text.strip() if description_elem else 'N/A'

        book_info = {
            'title': title_elem.text.strip() if title_elem else 'N/A',
            'author': author_elem.text.strip() if author_elem else 'N/A',
            'average_rating': avg_rating,
            'ratings_count': ratings_count,
            'published_year': published_year,
            'description': description,
        }

        books.append(book_info)

    return books

def print_scraped_books(scraped_books):
    for book in scraped_books:
        print("Book Information:")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Average Rating: {book['average_rating']}")
        print(f"Ratings Count: {book['ratings_count']}")
        print(f"Published Year: {book['published_year']}")
        print(f"Description: {book['description']}")
        print("---")

def main():
    # Replace 'https://www.goodreads.com/search?page=99&q=books&qid=I5rZPmqzTS&tab=books' 
    # with the actual URL of the search page you want to scrape.
    url_to_scrape = 'https://www.goodreads.com/search?page=99&q=books&qid=I5rZPmqzTS&tab=books'
    
    # get the data without selenium
    scraped_books = scrape_books(url_to_scrape)
    
    # print info in terminal
    print_scraped_books(scraped_books)

main()