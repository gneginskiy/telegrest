# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5001 available to the world outside this container
EXPOSE 5001
# Set PYTHONPATH to app/src/
ENV PYTHONPATH /app/
# Run app.py when the container launches
CMD ["python", "src/main.py"]

