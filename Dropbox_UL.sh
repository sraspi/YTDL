#!/bin/bash 
echo "Start Dropbox upload"
cd /home/pi/Dropbox-Uploader/Dropbox/mp3 && /home/pi/Dropbox-Uploader/Dropbox/dropbox_uploader.sh upload *.mp3 /mp3
