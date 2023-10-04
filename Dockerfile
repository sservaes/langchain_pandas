FROM python:3.9-slim

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Update
RUN apt-get update && apt-get install -y gcc

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]