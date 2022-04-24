# flask-restful-docker

## Service build

### Build image

    docker build . -t flask-restful:latest

### Compose up

    docker-compose up -d

## API usage

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
