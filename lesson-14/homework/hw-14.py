# JSON Parsing
import json

with open('students.json', 'r') as file:
    data = json.load(file)
    for student in data['students']:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Weather API
import requests

city = "Tashkent"
api_key = "your_api_key_here"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather = response.json()

print(f"Temperature: {weather['main']['temp']}°C")
print(f"Humidity: {weather['main']['humidity']}%")
print(f"Weather: {weather['weather'][0]['description']}")

# JSON Modification
import json

filename = 'books.json'

def load_books():
    with open(filename, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(filename, 'w') as f:
        json.dump(books, f, indent=4)

def add_book(book):
    books = load_books()
    books.append(book)
    save_books(books)

def update_book(title, updated_info):
    books = load_books()
    for book in books:
        if book['title'] == title:
            book.update(updated_info)
    save_books(books)

def delete_book(title):
    books = load_books()
    books = [book for book in books if book['title'] != title]
    save_books(books)

# Movie Recommendation System
import requests
import random

api_key = "asdfqwk.api"
genre = input("Enter movie genre: ")

url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}"

response = requests.get(url)
movies = response.json().get('Search', [])

if movies:
    movie = random.choice(movies)
    print(f"Title: {movie['Title']}")
    print(f"Year: {movie['Year']}")
else:
    print("No movies found for this genre.")
