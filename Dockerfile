# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install "git+https://github.com/LahiLuk/YouTokenToMe" -r requirements.txt

# command to run the app using uvicorn.
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]