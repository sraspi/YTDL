#!/bin/sh
#bootjobs.sh
cd
cd /home/pi/noip-2.1.9-1
sudo noip2
cd
sleep 6.0
sudo mount -a
echo "NAS mounted"
cd /home/pi/Dropbox-Uploader/Dropbox/
python3 I_YTDL4.5.py
