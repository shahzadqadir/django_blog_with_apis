# pull docker image
FROM python:3.10

# setup environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /code

# copy dependency files
COPY Pipfile Pipfile.lock /code/

# install pipenv and dependencies
RUN pip install pipenv && pipenv install --system

# copy rest of files to docker
COPY . /code/