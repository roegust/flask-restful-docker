# flask-restful-docker

## Service build

### Build image

    docker build . -t flask-restful:latest

### Start container

    docker run -p 5000:5000 flask-restful

## APi usage

`GET /task`

`GET /task/<id>`

`POST /task`

    {
      "name": <name>
    }

`PUT /task/<id>`

    {
      "name": <name>
      "status": <status>
    }

`DELETE /task/<id>`
