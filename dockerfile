# Python docker image (using 3.11-slim)
FROM python:3.11-slim

# Set folder kerja
WORKDIR /aplikasi

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command
CMD ["python", "main.py"]