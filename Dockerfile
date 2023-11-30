# Use an official Python runtime as a parent image
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt

RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
