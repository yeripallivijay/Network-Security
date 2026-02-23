FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

# Install system dependencies (if needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI via pip (cleaner for slim images)
RUN pip install --no-cache-dir awscli

CMD ["python3", "app.py"]