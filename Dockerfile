# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip3 install Flask==2.2.2
RUN pip3 install pymongo==3.11.4
RUN pip3 install Jinja2==3.0.3

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py", "--host=0.0.0.0"]

