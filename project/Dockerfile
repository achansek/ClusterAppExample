#From https://towardsdatascience.com/docker-for-python-dash-r-shiny-6097c8998506
# Also From https://towardsdatascience.com/deploy-containerized-plotly-dash-app-to-heroku-with-ci-cd-f82ca833375c
FROM python:3.9-slim-buster

LABEL maintainer "Aravind Chandrasekaran aravindcsn@gmail.com"

# set working directory in container
WORKDIR /usr/src/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY /app /usr/src/app/

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally
CMD gunicorn --bind 0.0.0.0:8050 app:server