# Use Python base image
FROM python:3.9-slim

# Set work dir
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy code
COPY app.py .

# Run app
CMD ["python", "app.py"]
