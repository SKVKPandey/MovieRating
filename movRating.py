import sqlite3
import pandas as pd
from tabulate import tabulate

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('movie_ratings.db')
cursor = conn.cursor()

# Create tables for movies and reviews
cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre TEXT,
                    release_year INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_id INTEGER,
                    user_name TEXT,
                    rating INTEGER,
                    review TEXT,
                    FOREIGN KEY(movie_id) REFERENCES movies(id)
                )''')

conn.commit()
print("Database setup complete!")

# Function to add a movie to the database
def add_movie(title, genre, release_year):
    cursor.execute('INSERT INTO movies (title, genre, release_year) VALUES (?, ?, ?)',
                   (title, genre, release_year))
    conn.commit()
    print(f"Movie '{title}' added successfully!")

# Function to add a review and rating for a movie
def add_review(movie_title, user_name, rating, review):
    cursor.execute('SELECT id FROM movies WHERE title = ?', (movie_title,))
    movie = cursor.fetchone()
    if movie:
        movie_id = movie[0]
        cursor.execute('INSERT INTO reviews (movie_id, user_name, rating, review) VALUES (?, ?, ?, ?)',
                       (movie_id, user_name, rating, review))
        conn.commit()
        print(f"Review added for '{movie_title}' by {user_name}")
    else:
        print(f"Movie '{movie_title}' not found!")

# Function to view all movies
def view_movies():
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    for movie in movies:
        print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Release Year: {movie[3]}")

# Function to search for a movie by title
def search_movie(title):
    cursor.execute('SELECT * FROM movies WHERE title LIKE ?', ('%' + title + '%',))
    movies = cursor.fetchall()
    if movies:
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Release Year: {movie[3]}")
    else:
        print("No movie found with that title.")

# Function to generate movie recommendations based on average rating
def get_recommendations():
    cursor.execute('''SELECT movies.title, AVG(reviews.rating) as avg_rating, COUNT(reviews.id) as total_reviews
                      FROM reviews
                      INNER JOIN movies ON movies.id = reviews.movie_id
                      GROUP BY movies.title
                      HAVING total_reviews > 1
                      ORDER BY avg_rating DESC''')
    
    recommendations = cursor.fetchall()
    if recommendations:
        df = pd.DataFrame(recommendations, columns=['Title', 'Average Rating', 'Total Reviews'])
        print(tabulate(df, headers='keys', tablefmt='psql'))
    else:
        print("No recommendations available yet.")

# Main function to interact with the system
def main():
    while True:
        print("\n--- Movie Rating System ---")
        print("1. Add Movie")
        print("2. Add Review")
        print("3. View Movies")
        print("4. Search Movie")
        print("5. Get Recommendations")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Movie Title: ")
            genre = input("Genre: ")
            release_year = int(input("Release Year: "))
            add_movie(title, genre, release_year)
            
        elif choice == "2":
            movie_title = input("Movie Title: ")
            user_name = input("Your Name: ")
            rating = int(input("Rating (1-10): "))
            review = input("Your Review: ")
            add_review(movie_title, user_name, rating, review)
            
        elif choice == "3":
            view_movies()
            
        elif choice == "4":
            title = input("Search Movie Title: ")
            search_movie(title)
            
        elif choice == "5":
            get_recommendations()
            
        elif choice == "6":
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
