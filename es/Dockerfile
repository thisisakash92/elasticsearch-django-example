
FROM python:3.4

# Make working directory
RUN mkdir /es
WORKDIR /es

# Copy project to docker work directory
ADD . /es

RUN pip install -r requirements.txt

# Expose django port
EXPOSE 8000

