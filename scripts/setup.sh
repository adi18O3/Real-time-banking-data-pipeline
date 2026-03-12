#!/bin/bash

echo "======================================"
echo "Setting up Banking Big Data Pipeline"
echo "======================================"

# Update packages
sudo apt update

# Install Java
sudo apt install openjdk-17-jdk -y

# Install Python dependencies
sudo apt install python3-pip python3-pandas -y

# Install Docker
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker

# Install Spark
cd ~

if [ ! -d "spark" ]; then
    wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
    tar -xvzf spark-3.5.1-bin-hadoop3.tgz
    mv spark-3.5.1-bin-hadoop3 spark
fi

# Add Spark to PATH
echo 'export SPARK_HOME=$HOME/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc

source ~/.bashrc

echo "Setup Complete!"
