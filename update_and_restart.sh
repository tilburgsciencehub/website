#!/bin/bash

# Define variables
REPO_URL="https://github.com/tilburgsciencehub/website-flask.git"
CLONE_DIR="/home/ubuntu/tsh-flask"

# Stop the existing Docker containers
docker compose -f $CLONE_DIR/docker-compose.yml down

# Remove the existing repository (optional: make sure you want to do this)
rm -rf $CLONE_DIR

# Clone the repository
git clone $REPO_URL $CLONE_DIR

# Navigate to the clone directory
cd $CLONE_DIR

# Build the Docker containers
docker compose build

# Start the Docker containers
docker compose up -d

# Clean unused docker images
docker system prune -a -f
