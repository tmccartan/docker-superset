FROM python:3.6

# Superset version
ARG SUPERSET_VERSION=0.29.0rc7

# Configure environment
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/etc/superset:/home/superset:$PYTHONPATH \
    SUPERSET_REPO=apache/incubator-superset \
    SUPERSET_VERSION=${SUPERSET_VERSION} \
    SUPERSET_HOME=/var/lib/superset

# Create superset user & install dependencies
RUN useradd -U -m superset && \
    mkdir /etc/superset  && \
    mkdir ${SUPERSET_HOME} && \
    chown -R superset:superset /etc/superset && \
    chown -R superset:superset ${SUPERSET_HOME} && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        curl \
        default-libmysqlclient-dev \
        freetds-dev \
        freetds-bin \
        libffi-dev \
        libldap2-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

COPY requirements.txt ${SUPERSET_HOME}/

RUN pip install --no-cache-dir -r ${SUPERSET_HOME}/requirements.txt && \
    pip install --no-cache-dir superset==${SUPERSET_VERSION}

# Configure Filesystem
COPY config /etc/superset
COPY scripts /home/superset
RUN chmod +x /home/superset/entrypoint.sh
RUN chmod +x /home/superset/superset-init.sh

WORKDIR /home/superset

# Deploy application
EXPOSE 8088
CMD ["./entrypoint.sh"]
USER superset
