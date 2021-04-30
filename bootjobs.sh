#!/bin/sh
#bootjobs.sh
cd
cd /home/pi/noip-2.1.9-1
sudo noip2
cd
sleep 60
sudo mount -a
echo "NAS mounted"
cd /home/pi/Dropbox-Uploader/Dropbox/
sh YTDL-launcher.sh
