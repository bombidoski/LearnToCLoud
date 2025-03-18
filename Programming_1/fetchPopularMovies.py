import requests
import json

API_KEY = '19cf4d21af4b66e75657df5cefb142a1'   #  API key from TMDB
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

if __name__ == '__main__':
    movies = fetch_popular_movies()
    transformed_movies = [transform_movie_data(movie) for movie in movies]
    
    # Save the transformed data to a JSON file
    with open('popular_movies.json', 'w') as f:
        json.dump(transformed_movies, f, indent=2)
    
    print('Transformed movie data saved to popular_movies.json')
