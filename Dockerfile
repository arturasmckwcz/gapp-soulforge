FROM python:3.9

# Set the working directory
WORKDIR /app

# Install any required dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the entry point for the container
CMD ["watchmedo", "auto-restart", "--recursive", "--patterns=*.py", "--", "python", "app.py"]
