# Python elastic API infrastructure environment

The following is a quick and dirty Python-Elasticsearch environment for validating
Elasticsearch interactions. It gives you the ability to build, run and trouble shoot
with a fully isolated environment.

## Requirements

All that is required is the ability to run Docker and Docker Compose and access
to the internet.

## Usage

While all actions can be performed via `docker-compose`, we have provided some
quick helpers:

- start : create and standup the docker images, with the last built api image.
- pause : stops the running containers. This allows for limited persistance.
- kill : Stops and destroy the running containers. All container only data is deleted.

- build : build a new image of the python api app
- restart : Restart all containers. Use it to refresh the python container after a build

- status : Show the status of the running containers
- logs : tail the logs from all the containers

- login : Opens a console in the python container. NOTE: Any changes here are lost.

## Notes:

### Workflow

I have tried to simplify the workflow. :

1. ./build
2. ./start
3. ./logs

On a change, you can also :

1. ./build
2. ./restart

### Endpoints

The conatiners have been built so the endpoints are usable inside and outside the containers.

|   End Point   |  URL outisde   |     URL inside     |
|---------------|----------------|--------------------|
| Kibana        | [localhost:5601](localhost:5601) | kibana:5601        |
| Python API    | [localhost:5000](localhost:5000) | python-runner:5000 |
| Elasticsearch | [localhost:9200](localhost:9200) | elasticsearch:9200 |


### Swagger API

The Python FlaskREST+ is a flask API extension that will allow for a self documenting
API written in swagger. See [FlaskREST+](http://flask-restplus.readthedocs.io/en/stable/index.html)
and [Swagger](https://swagger.io) for additional information.

The python endpoint can also supply the [Swagger definition](http://localhost:5000/swagger.json)
to build other client software.
