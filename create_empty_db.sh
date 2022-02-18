#!/bin/bash

# Go to the flask directory
cd ~/flaskapp/flask

# Start app environment
source ../set_environment_vars.sh
source env/bin/activate

# Remove the existing database
rm app/webapp.db

# Execute python script to create the new database
python3 create_webapp_db.py











