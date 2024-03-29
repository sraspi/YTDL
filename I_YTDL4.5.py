#!/usr/bin/python3.8

#Prozesszeit wird geloggt, Email taeglich, Error-mail included, error 403-fixed, NAS_error.log(1), unable to extract uploader ID fixed, s. code Stand 13.03.2023, cronjobs error fixed, pw deleted
from __future__ import unicode_literals
import subprocess
#import youtube_dl
import yt_dlp
import urllib
import shutil
import os
import sys
import time
from datetime import datetime
import pytz
import smtplib, ssl
import email
import smbus
import sendmail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#Startzeit des Prozesses festlegen:
t1 = datetime.now(pytz.utc)

# Dateiname des logfiles:
Dateiname = ("/home/pi/Dropbox-Uploader/Dropbox/logfile.txt")
errorlog = ("/home/pi/Dropbox-Uploader/Dropbox/errorlog.txt")
print()
print("Python-version:", sys.version)
print()
print()
#delete local mp3-folder and create new mp3-folder
print("YTDL4.5.py startet (included backups and YT-cache error-handling)")
print()
print()
print("delete local mp3/mp4 folder")
shutil.rmtree('/home/pi/Dropbox-Uploader/Dropbox/mp3', ignore_errors=True)
os.mkdir("/home/pi/Dropbox-Uploader/Dropbox/mp3")
shutil.rmtree('/home/pi/Dropbox-Uploader/Dropbox/mp4', ignore_errors=True)
os.mkdir("/home/pi/Dropbox-Uploader/Dropbox/mp4")
print("done!")
print()

while True:    
  # Dropbox txt-files runterladen aus /mp4:
  subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Dropbox_DL.sh")

  #Anzahl der Downloads ermitteln:
  a = "/home/pi/Dropbox-Uploader/Dropbox/mp4" #Pfadangabe zum Ordner mp4
  b = "/home/pi/Dropbox-Uploader/Dropbox/mp3" #Pfadangabe zum Ordner mp3
  m = os.listdir(a)
  
  n =len(m) # Anzahl der Dateien im Ordner bestimmen
  print("Anzahl der Dateien Dropbox:", n)
  print()

  #Schleife zum Youtube-dl und mp3-merge:
  i = 0
  e = 0
  while i < n:
    filename = "/home/pi/Dropbox-Uploader/Dropbox/mp4/" + m[i]
    f = open(filename), 'r'# txt-Datei oeffnen
  
    
  
    with open(filename) as fp:
     try:
         url = fp.read() #Inhalt der Textdatei lesen
         print("Download: ", url)
         print()
     except:
         print("Dropbox-error:  no valid url!!!")
         timestr = time.strftime("%Y%m%d-%H%M%S")
         fobj_out = open(errorlog,"a")
         fobj_out.write(timestr + ": txt-error, no valid txt: " + '\n')
         fobj_out.close()
        
     
   
    subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/clear_cache.sh") 
  # Youtube download und merge to mp3
    ydl_opts = {
       #'verbose': '--',
       #' cachedir': '--no-cache-dir',
      'format': 'bestaudio/best',
      'outtmpl': '/home/pi/Dropbox-Uploader/Dropbox/mp3/%(title)s.%(ext)s',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
          }],

    }  
  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
#with youtube_dl.YoutubeDL(ydl_opts) as ydl: --------------------funktioniert seit Anfang 2023 nicht mehr, deswegen import yt_dlp, vorher mit pip3 installiert
#/usr/local/lib/python3.5/dist-packages/yt_dlp/extractor $ sudo nano youtube.py
#mit strg w Zeile gesucht: 'uploader_id': self._search_regex(r'/(?:channel/|user/|(?=@))([^/?&#]+)', owner_profile_url, 'uploader id', default=None),
#und geaendert(Zeile hier ist schon korrekt
          try:
              info_dict = ydl.extract_info(url, download=True)
              o = os.listdir(b)
              trackname = o[i]
              print()
              print("Add to logfile.txt: Track ",i , trackname, "added to logfile.txt")
              #logfile schreiben:
              print()      
              timestr = time.strftime("%Y%m%d-%H%M%S")
              fobj_out = open(Dateiname,"a" )
              fobj_out.write("YTDL4.2.py: " + timestr + ", " + trackname + ",        " + "url: " + url + '\n')
              fobj_out.close()
              print("logfile appended", trackname)
              i = i +1
              
          
        
          #subprocess.call("/home/pi/merge_mp3.sh") # merge ist offensichtlich nicht mehr gueltig? waere hier!
        
          
          except:
              print()
              timestr = time.strftime("%Y%m%d-%H%M%S")
              error = sys.exc_info()[1]
              print(str(error))
              fobj_out = open(Dateiname,"a")
              fobj_out.write(timestr + ": YTDL-error: " + str(error) + filename + "   url: " + url + '\n')
              fobj_out.close()      
              
              
              subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Error-mail.sh")
              print(str(e))
              i = i + 1
              e = e + 1

    #Dropbox and backup upload, local backup at SD-
    print()
    print("Dropbox upload start")
    subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Dropbox_UL.sh")
    
    
    print() 
    print("proceed next youtube-download:")
           
  
    #delete mp4
  
    #filename_mp4 = "/home/pi/Dropbox-Uploader/Dropbox/mp4/" + m[i]
    #f = open(filename_mp4)# Datei oeffnen
    #os.remove(filename_mp4)
    #print("delete",filename_mp4 )
    
  
  
   
  
  #delete lokal mp3-folder and create new mp3-folder
  print("all YT-downloads finished")
  print()
  print()
  subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/local_BA.sh")
  print()
  print("Dropbox-backup started")
  subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Dropbox_BA.sh")
  print()
  print()
  print("delete + create new local mp3/mp4-folder")
  shutil.rmtree('/home/pi/Dropbox-Uploader/Dropbox/mp3', ignore_errors=True)
  os.mkdir("/home/pi/Dropbox-Uploader/Dropbox/mp3")
  shutil.rmtree('/home/pi/Dropbox-Uploader/Dropbox/mp4', ignore_errors=True)
  os.mkdir("/home/pi/Dropbox-Uploader/Dropbox/mp4")
  print("done!")

  print()
  
  
  print("delete and create new dropbox/mp4 folder:")
  subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Dropbox_del.sh")
  subprocess.call("/home/pi/Dropbox-Uploader/Dropbox/Dropbox_mkdir.sh")
  print()
  print("done!")
  
  #calculate uploaded dropbox-files and totalprocess-duration:
  print()
  t2 = datetime.now(pytz.utc)
  t_diff = t2 -t1
  n = n - e
  timestr = time.strftime("%Y%m%d-%H%M%S")

  print("overrride error.log with 1")
  f = open("/home/pi/NAS/error.log", "w")
  f.write("1")
  f.close()
  print("YTDL NAS 1 written")

  fobj_out = open(Dateiname,"a" )
  fobj_out.write('\n' + timestr + ": " + "PROCESS NORMAL FINISHED, required process-time:" + str(t_diff) + '\n' + '--------------------------------------' + '\n')
  fobj_out.close()
  print(timestr, ": ", n, "Tracks processed! required process-time:", t_diff)
  try:
      sendmail.sendmail()
  except:
      print("error sendmail")
  
  
  sys.exit()
