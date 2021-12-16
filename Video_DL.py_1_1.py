from __future__ import unicode_literals
import youtube_dl

while True:
    url = input("Video-Link eingeben:")
    print (url, "youtube download started")


    ydl_opts = {
    
        'outtmpl': '/home/lenovo/Videos/%(title)s.%(ext)s',
        }  
  
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
          

   
    
 
       
    

