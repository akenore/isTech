# Use an official Python runtime as a parent image
FROM python:3.14-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Set the working directory to the Django project root (where manage.py is)
WORKDIR /app/app

# Collect static files
# Force DEBUG=False so STATIC_ROOT is used
RUN DEBUG=False SECRET_KEY='collectstatic-dummy-key' python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Run gunicorn
# Now that we are in /app/app, config.wsgi is directly importable
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
