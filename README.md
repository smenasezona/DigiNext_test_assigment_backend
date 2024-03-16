# Test assignment in DigiNext (backend)

#### Done by: [Kiyashko Artsiom](https://career.habr.com/kiyashko_artsiom)
#### Email: *artemkiasko@gmail.com*

## Documentation for Flask API with SQLite Database

This document provides a comprehensive guide to understanding and utilizing the Flask API with SQLite database for managing entities. The API allows creating, retrieving, updating, and deleting entities, as well as filtering entities by labels and retrieving coordinates.

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Endpoints](#endpoints)
    - [Create Entity](#create-entity)
    - [Get Entity](#get-entity)
    - [Update Entity](#update-entity)
    - [Delete Entity](#delete-entity)
    - [Get All Entities](#get-all-entities)
    - [Filter Entities](#filter-entities)
    - [Get Coordinates](#get-coordinates)

### Introduction

This Flask API serves as a backend for managing entities. It provides endpoints to perform CRUD operations on entities stored in an SQLite database. Each entity consists of a name, coordinate, and labels.

### Setup

Ensure you have Python and Flask installed. Additionally, make sure to install the required packages by running:

``pip install Flask flask-cors
``

The SQLite database file, identifier.sqlite, will be created automatically in the same directory as the main.py file when you run the Flask application.

## Endpoints

### Create Entity

* URL: /entities
* Method: POST
* Request Body: JSON

```json
{
  "name": "entity_name",
  "coordinate": "x,y",
  "labels": "label1,label2"
}
```

* Response : 
  * Status Code: 201 Created
  * JSON Data:

```json
{
  "message": "Entity created successfully"
}
```

### Get Entity

* URL: /entities/{name}
* Method: GET
* Response:
  * Status Code: 200 OK (if found), 404 Not Found (if not found)
  *  JSON Data (if found): 
  
```json
{
  "name": "entity_name",
  "coordinate": "x,y",
  "labels": "label1,label2"
}
```
### Update Entity

* URL: /entities/{name}
* Method: PUT
* Request Body: JSON

```json
{
  "coordinate": "new_x,new_y",
  "labels": "new_label1,new_label2"
}
```

* Response:
  * Status Code: 200 OK
  * JSON Data:
```json
{
  "message": "Entity updated successfully"
}
```

### Delete Entity

* URL: /entities/{name}
* Method: DELETE
* Response:
  * Status Code: 200 OK
  * JSON Data:
```json
{
  "message": "Entity deleted successfully"
}
```

### Get All Entities

* URL: /entities
* Method: GET
* Response:
  * Status Code: 200 OK
  * JSON Data:
```json
[
  {
    "name": "entity_name",
    "coordinate": "x,y",
    "labels": "label1,label2"
  }
]
```
### Filter Entities

* URL: /entities/filter/{label}
* Method: GET
* Response: 
  * Status Code: 200 OK
  * JSON Data:
```json
[
  {
    "name": "entity_name",
    "coordinate": "x,y",
    "labels": "label1,label2"
  }
]
```

### Get Coordinates
* URL: /coordinates
* Method: GET
* Response:
  * Status Code: 200 OK
  * JSON Data:
```json
{
    "coordinates": [
        ["x1", "y1"],
        ["x2", "y2"]
    ]
}
```

