# Popular Movies API

This project is a serverless REST API for retrieving information about popular movies. The API is hosted on Azure and leverages services such as CosmosDB, MongoDB, Azure Function, and TMDB API. It provides an endpoint to list all the popular movies in an arranged format.

## Project Overview

The Popular movies API allows clients to:
1. Retrieve a list of all movies including titles, releaseyear, genre and cover images.

 ## Infrastructure

The application stack includes the following components:
- **Azure Functions**: serverless compute service to host Python functions (GetMovies) and enable an API interface.
- **Azure Cosmos DB (with MongoDB API)**: Stored the movie data fetched from TMDB in Cosmos DB using its MongoDB compatibility..
- **Azure Blob Storage**: Stored the movie cover images fetched from TMDB..
- **Azure Functions**: Processed API requests (GetMovies), Interacted with Cosmos DB, and Blob Storage to handle data processing and retrieval..

## Data Model

Each movie entry in the CosmosDB database follows this structure:
```json
{
    "title": movie["title"],
    "releaseYear": movie["release_date"].split("-")[0],
    "genre": ", ".join(map(str, movie["genre_ids"])),  // Optionally map genre IDs to genre names
    "coverUrl": f"https://image.tmdb.org/t/p/w500{movie["poster_path"]}"
}
```

## Endpoints

1. **GET/GetMovies**

    **Description**: Retrieves a list of all music albums.  
    **Response**: Returns an array of movies, each with titles, releaseYear, genre and cover cover_url.

    **Example response**:
    ```json
    [
        {
            "title": "The Gorge",
            "releaseYear": "2025",
            "genre": "10749, 878, 53",
            "coverUrl": "https://image.tmdb.org/t/p/w500/7iMBZzVZtG0oBug4TfqDb9ZxAOa.jpg"
        },
        {
            "title": "Flight Risk",
            "releaseYear": "2025",
            "genre": "28, 53, 80",
            "coverUrl": "https://image.tmdb.org/t/p/w500/q0bCG4NX32iIEsRFZqRtuvzNCyZ.jpg"
        },
    ]
    ```

## Usage
 
    Examples:
         http://localhost:7071/api/GetMovies
