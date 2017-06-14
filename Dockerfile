FROM python:3.4

# File Author / Maintainer
MAINTAINER Akash akash@inzyte.com

# Non buffered mode
ENV PYTHONUNBUFFERED 1

# Force root mode to run celery
ENV C_FORCE_ROOT "yes"

# Make working directory
RUN mkdir /es
WORKDIR /es

# Copy project to docker work directory
ADD . /es

# install project requirements
RUN pip install -r requirements.txt

# Expose django port
EXPOSE 8000

