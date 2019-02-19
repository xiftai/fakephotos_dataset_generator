#!/usr/bin/python3

import os
import time
import requests
import bs4
           
max_images = 1000 
photos_dir = "fakephotos"

os.makedirs(photos_dir, exist_ok=True)

for x in range(max_images): 
    print("Downloading fake photo " + str(x+1) + "/" + str(max_images))
    res = requests.get('https://thispersondoesnotexist.com')
    res.raise_for_status()
    imageName = "fakephoto%d.jpg" % x

    imageFile = open(os.path.join(photos_dir, imageName), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    time.sleep(0.5)

print('Finished.')
