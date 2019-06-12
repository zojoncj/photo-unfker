#! /usr/bin/env python
import os

from PIL import Image
import exifread
loc = "D:\Piox"



for subdir, dirs, files in os.walk(loc):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        print(filepath)
        try:
            im = Image.open(filepath)
        except:
            continue
        tags = {}
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        print(tags['Image Model'])


 
    
    