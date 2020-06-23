'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-15"
-------------------------------------------------------
'''
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = str(input('Title: '))
    year = int(input('Year of Release:'))
    director = str(input('Director: '))
    rating= float(input('Rating: '))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    return movie
    # Your code here

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    line = line.split('|')
    title = line[0]
    year = int(line[1])
    director = (line[2])
    rating = float(line[3])
    genres = []
    
    for genre_code in line[4].split(','):
        genres.append(int(genre_code))
    movie = Movie(title, year, director, rating, genres)
        
    # Your code here

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    movies = []
     
    for line in fv:
        movie = read_movie(line)
        movies.append(movie)
    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """
    print('Genres')
    for i in range(len(Movie.GENRES)):
        print( '{:d}: {:s}'.format(i, Movie.GENRES[i]))

    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
#     print(menu())
    menu()
    user_val = ' '
    genres = []
    while user_val != '' or len(genres) < 1:
        user_val = input('Enter a genre number (ENTER to quit): ')
        if user_val.isdigit():
            user_val = int(user_val)
            if 0 <= user_val < 10:
                if user_val not in genres:
                    genres.append(user_val)
                else:
                    print('Error: genre already chosen')
            else:
                print('Error: input must be less than 10')
        elif user_val == '':
            #GET RID OF
            genres.sort()
            return genres
        else:
            print('Error: not a positive number.')
    genres.sort()
    return genres
        


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies =[]
    for movie in movies:
        if movie.rating >= rating:
            rmovies.append(movie)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for movie in movies:
        if genre in movie.genres:
            gmovies.append(movie)
        
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    for movie in movies:
        if genres == movie.genres:
            gmovies.append(movie)
        
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = [0] * len(Movie.GENRES)
    for movie in movies:
        for genre in movie.genres:
            counts[genre] += 1

    return counts