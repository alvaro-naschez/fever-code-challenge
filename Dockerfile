
ARG PYTHON_VERSION=3.10.9
ARG POETRY_VERSION=1.3.1

FROM python:$PYTHON_VERSION as base

WORKDIR /app
ENV PYTHONPATH=/app

COPY poetry.lock pyproject.toml ./

# RUN pip install 'poetry==${POETRY_VERSION}'
RUN pip install 'poetry==1.3.1'

RUN poetry install --no-dev

################################################################################

FROM base as api

COPY fever fever


################################################################################

FROM base as reader

COPY fever fever


################################################################################

FROM base as migration

COPY fever fever

COPY alembic  alembic
COPY alembic.ini .
