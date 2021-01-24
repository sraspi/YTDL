#!/bin/bash 
echo "Start Dropbox download"
cd /home/pi/Dropbox-Uploader/Dropbox/ && ./dropbox_uploader.sh download /mp4 /home/pi/Dropbox-Uploader/Dropbox
