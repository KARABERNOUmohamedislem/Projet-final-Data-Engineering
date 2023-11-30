FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to optimize caching
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python", "app.py"]
