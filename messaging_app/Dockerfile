# Use official Python image as base
FROM python:3.11-slim-bullseye

# Upgrade system packages to fix vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Start the application (replace with your actual start command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]