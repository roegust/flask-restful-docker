# flask-restful-docker

## Service build

### Build image

    docker build . -t flask-restful:latest

### Compose up

    docker-compose up -d

then you can access api in http://127.0.0.1/task

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
