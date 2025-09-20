#!/bin/bash
echo "Setting up Flask app..."

cd /home/ec2-user/database_lab

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

sudo systemctl start flaskapp