#!/bin/bash

# Install required packages for RPi
sudo apt-get install libopenblas-dev libportaudio2 python3-pip python3-virtualenv

# This config works for my USB Soundcard, might be different for you
# https://superuser.com/questions/626606/how-to-make-alsa-pick-a-preferred-sound-device-automatically
sudo cp ./setup_files/asound.conf /etc/

# Setup the virtual environment for python
virtualenv env
source env/bin/activate

# Install required packages
pip install -r requirements.txt

# "Create" the service and start and enable it
sudo cp ./setup_files/reprec.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now reprec.service
