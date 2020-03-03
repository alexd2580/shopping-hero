# For reference see https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
FROM python:3.7.6-alpine3.11 as builder

# ENV PIP_DEFAULT_TIMEOUT=100 \
#     PIP_DISABLE_PIP_VERSION_CHECK=1 \
#     PIP_NO_CACHE_DIR=1 \
ENV POETRY_VERSION=1.0.5

WORKDIR /app

# Install poetry and set up a venv.
RUN apk add --no-cache musl-dev gcc make libffi-dev openssl-dev python3-dev
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv venv

# Install dependencies.
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | venv/bin/pip install -r /dev/stdin

# Copy the app code, build it with poetry (why?) and install to the venv?
COPY app ./app
RUN poetry build && venv/bin/pip install dist/*.whl

# For reference see: https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker
FROM tiangolo/uvicorn-gunicorn-starlette:python3.7
COPY --from=builder /app/venv /app
