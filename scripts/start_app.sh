#!/bin/bash

# Set environment variable
export APP_ENV=$DEPLOYMENT_GROUP_NAME

# Run the python app
python3 /home/ec2-user/app/app.py