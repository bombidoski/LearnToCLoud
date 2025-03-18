# Popular Movies API

This project is a serverless REST API for retrieving information about popular movies. The API is hosted on Azure and leverages services such as CosmosDB, MongoDB, Azure Function, and TMDB API. It provides an endpoint to list all the popular movies in an arranged format.

## Project Overview

The Popular movies API allows clients to:
1. Retrieve a list of all movies including titles, releaseyeaer, genre and cover images.


## Infrastructure

The application stack includes the following components:
- **Azure Functions**: serverless compute service to host Python functions (GetMovies) and enable an API interface.
- **S3**: Stores cover images for each album.
- **Lambda**: Serverless functions that handle API requests.
- **API Gateway**: Exposes API endpoints to interact with Lambda functions.

## Data Model

Each album entry in the DynamoDB database follows this structure:
```json
{
    "album_id": "unique-album-id",
    "title": "Album Title",
    "artist": "Artist Name",
    "genre": "Genre",
    "release_year": "Year of Release",
    "cover_url": "https://s3.amazonaws.com/your-bucket-name/album-cover.jpg"
}
```


## Endpoints

1. **GET /getalbums**

    **Description**: Retrieves a list of all music albums.  
    **Response**: Returns an array of albums, each with title, artist, genre, release_year, and cover_url.

    **Example response**:
    ```json
    [
        {
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": "1969",
            "cover_url": "https://s3.amazonaws.com/your-bucket-name/abbey-road.jpg"
        },
        {
            "title": "Thriller",
            "artist": "Michael Jackson",
            "genre": "Pop",
            "release_year": "1982",
            "cover_url": "https://s3.amazonaws.com/your-bucket-name/thriller.jpg"
        }
    ]
    ```

2. **GET /albumsbyyear/{year}**

    **Description**: Retrieves albums released in a specific year.  
    **Path Parameter**: `year` – The release year of albums you want to retrieve.  
    **Response**: Returns an array of albums that match the specified release year.

    **Example response for /albums/1982**:
    ```json
    [
        {
            "title": "Thriller",
            "artist": "Michael Jackson",
            "genre": "Pop",
            "release_year": "1982",
            "cover_url": "https://s3.amazonaws.com/your-bucket-name/thriller.jpg"
        }
    ]
    ```

## Usage
 
    Examples:
         https://api.shoiyan.com/getalbums
         https://api.shoiyan.com/getalbumsbyyear/year
