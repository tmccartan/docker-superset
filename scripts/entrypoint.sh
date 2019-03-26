#!/usr/bin/env bash

export GUNICORN_WORKERS=$((2 * $(getconf _NPROCESSORS_ONLN) + 1))
export GUNICORN_BIND=0.0.0.0:8088 
export GUNICORN_LIMIT_REQUEST_FIELD_SIZE=0 
export GUNICORN_LIMIT_REQUEST_LINE=0 
export GUNICORN_TIMEOUT=120 


gunicorn --bind $GUNICORN_BIND  \
    --workers $GUNICORN_WORKERS \
    --timeout $GUNICORN_TIMEOUT \
    --limit-request-line $GUNICORN_LIMIT_REQUEST_LINE \
    --limit-request-field_size $GUNICORN_LIMIT_REQUEST_FIELD_SIZE \
    superset:app
