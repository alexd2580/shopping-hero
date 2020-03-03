FROM python:3.7.6-alpine3.11 as builder

ENV POETRY_VERSION=1.0.5

WORKDIR /build

# Install poetry and build dependency file.
RUN apk add --no-cache musl-dev gcc make libffi-dev openssl-dev
RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt

FROM tiangolo/uvicorn-gunicorn-starlette:python3.7

# Install dependencies.
COPY --from=builder /build/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# For reference see: https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker
RUN rm -rf /app/
COPY app /app/app
