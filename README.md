# Docker Superset

Dockerfile to build apache superset (0.29.0rc7) on a docker container.

# How to build 

``` docker build -t docker/superset .```

# Note on requirements

As per the rc, the version of cryptography is incompatible. So needed to list out the requirements from the github repo, this can be removed once the release version is changed.
