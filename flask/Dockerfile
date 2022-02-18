# Use the Python latest Debian bullseye image
FROM python:3.8.12-bullseye

# Install required applications
RUN apt-get update && apt-get upgrade -y && apt install nano -y

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]

