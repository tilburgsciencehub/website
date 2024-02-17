#!/bin/bash

# Check if the script is being run as a superuser
if [ "$EUID" -ne 0 ]; then
  echo "Please run the script as superuser (root)"
  exit 1
fi

# Step 1: Remove previous versions of Docker
apt-get remove -y docker docker-engine docker.io containerd runc

# Step 2: Update the package list
apt-get update

# Step 3: Install dependencies
apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Step 4: Create directory for Docker key
mkdir -p /etc/apt/keyrings

# Step 5: Add Docker GPG key
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Step 6: Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Step 7: Update the package list again
apt-get update

# Step 8: Install Docker
apt-get install -y docker-ce docker-ce-cli containerd.io

# Step 9: Add Docker group if it doesn't exist
if ! getent group docker > /dev/null; then
    groupadd docker
fi

# Step 10: Add user to Docker group
# This step is commented out to be manually executed if necessary
# usermod -aG docker <your-user-name>

# Step 11: Activate group changes
# This step is commented out to be manually executed if necessary
# newgrp docker

# Step 12: Verify Docker installation
docker run hello-world

echo "Docker installation complete."
