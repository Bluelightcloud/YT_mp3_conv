#!/usr/bin/env python
# coding: utf-8

# In[3]:


import youtube_dl
import sys

while True:
    url = input('Please enter the URL : ')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':  '%(title)s' + '.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
             'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(url, download=True)
    
    judge = input('Do you want to continue? (y/n)')
    if judge == 'n':
        print("終了します")
        sys.exit()


# In[ ]:




