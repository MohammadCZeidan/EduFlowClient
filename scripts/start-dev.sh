#!/bin/bash

# Development startup script for EduFlow

echo "Starting EduFlow in development mode..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env from env.example..."
    cp env.example .env
    echo "Please update .env with your credentials"
fi

# Start services with docker-compose
docker-compose up --build

