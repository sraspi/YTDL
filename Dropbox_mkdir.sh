#!/bin/bash 
echo "Create Dropbox mp4 folder"
cd /home/pi/Dropbox-Uploader/Dropbox/ && ./dropbox_uploader.sh mkdir /mp4 /home/pi/Dropbox-Uploader/Dropbox
