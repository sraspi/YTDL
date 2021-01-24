#!/bin/bash 
echo "delete Dropbox mp4 folder"
cd /home/pi/Dropbox-Uploader/Dropbox && ./dropbox_uploader.sh delete /mp4 /home/pi/Dropbox-Uploader/Dropbox
