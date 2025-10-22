# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Define usuário e diretório de trabalho
RUN useradd -m appuser
WORKDIR /app

# Install system dependencies required for psutil
RUN apt-get update && apt-get install -y gcc python3-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8081
USER appuser

HEALTHCHECK CMD curl -f http://localhost:8081/health || exit 1
# Command to run the application
CMD ["python", "app_status.py"]
