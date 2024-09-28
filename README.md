# MovieRating

This is a simple command-line-based **Movie Rating System** built with Python and SQLite that allows users to add movies, submit reviews, and get recommendations based on user ratings.

## Features:
- **Add Movies**: Users can add movies to the database, including details such as title, genre, and release year.
- **Add Reviews**: Users can rate movies and leave a review. Reviews are stored in the database and associated with their respective movies.
- **Search Movies**: Users can search for movies by their title, even with partial matches.
- **View Movies**: Display the full list of movies available in the database.
- **Get Recommendations**: Based on the average ratings and number of reviews, the system recommends top-rated movies.

## Installation:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/<your-github-username>/MovieRating.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MovieRating
    ```

3. Install the necessary Python dependencies:
    ```bash
    pip install pandas tabulate
    ```

4. Run the program:
    ```bash
    python movRating.py
    ```

## Requirements:
- Python 3.x
- SQLite (no external installation needed, built into Python)
- Pandas
- Tabulate

You can install the necessary dependencies using `pip`:
```bash
pip install pandas tabulate
```
## Usage:

Upon running the program, you will be presented with a menu offering the following options:
1. **Add Movie**: Enter movie details such as title, genre, and release year to add a new movie to the database.
2. **Add Review**: Provide the movie title, your name, a rating (between 1-10), and a short review.
3. **View Movies**: Displays a list of all movies stored in the database.
4. **Search Movie**: Allows you to search for a movie by entering part or all of its title.
5. **Get Recommendations**: Generates movie recommendations based on user ratings.
6. **Exit**: Exits the program.

## Example:

--- Movie Rating System ---

1. Add Movie
2. Add Review
3. View Movies
4. Search Movie
5. Get Recommendations
6. Exit Choose an option: 1 

Output: 
Movie Title: Inception Genre: Sci-Fi Release Year: 2010 Movie 'Inception' added successfully!


## License:

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing:

Feel free to fork this repository, submit issues, and make pull requests. Any contributions, such as adding new features or improving the code, are welcome.

