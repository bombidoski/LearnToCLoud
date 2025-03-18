import logging
import azure.functions as func
import requests
import json

API_KEY = '19cf4d21af4b66e75657df5cefb142a1'  #  TMDB API key
URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1'

def fetch_popular_movies():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()['results']
    else:
        raise Exception('Error fetching popular movies')

def transform_movie_data(movie):
    return {
        'title': movie['title'],
        'releaseYear': movie['release_date'].split('-')[0],
        'genre': ', '.join(map(str, movie['genre_ids'])),  # Optionally map genre IDs to genre names
        'coverUrl': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
    }

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GetMovies function processed a request.')

    try:
        # Fetch and transform popular movies
        movies = fetch_popular_movies()
        transformed_movies = [transform_movie_data(movie) for movie in movies]
        
        # Return the transformed movies as a JSON response
        return func.HttpResponse(
            body=json.dumps(transformed_movies, indent=2),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(
            "Failed to fetch or process movie data.",
            status_code=500
        )
