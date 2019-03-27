# Docker Superset

Dockerfile to build apache superset (0.29.0rc7) on a docker container. Superset is setup with a celery backend to process sqlab asyncronously 

# Config

To change superset configs, update the superset config file

# How to build 

``` docker build -t docker-superset .```

# How to run

Use the example docker compose file. 


# Note on requirements

As per the rc, the version of cryptography is incompatible. So needed to list out the requirements from the github repo, this can be removed once the release version is changed.
