FROM docker.artifactory.us.caas.oneadp.com/innerspace/python:3.8-slim-pipenv

LABEL maintainer "ADP DevSecOps: atkinskd <Ken.Atkins@adp.com>"

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential=12.9 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8080

WORKDIR  /

USER python

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY __version__.py __version__.py
COPY ./app /app

RUN pipenv install --deploy --system

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
