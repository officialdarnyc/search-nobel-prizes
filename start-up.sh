#!/bin/bash

# Run Docker Compose
docker-compose up -d

# Wait for the containers to start
sleep 5

# Run the Python script inside the container
docker exec python_app python ingest_data.py