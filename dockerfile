# Use the official Python image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5020

# Command to run the application
CMD ["python", "api.py"]