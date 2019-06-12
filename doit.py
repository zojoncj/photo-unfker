#! /usr/bin/env python
import os
import datetime
import hashlib

from PIL import Image
import exifread
from shutil import copyfile


loc = "D:\Piox"
dest = "E:\\new"

l={'EXIF ImageUniqueID','EXIF DateTimeOriginal','Image Model','Image ImageWidth','Image ImageLength'}

for subdir, dirs, files in os.walk(loc):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        fn, ext = os.path.splitext(file)
        try:
            im = Image.open(filepath)
        except:
            continue
        tags = {}
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        vals = {}
        name = path = ""
        if "EXIF DateTimeOriginal" in tags.keys():
          thething = str(tags['EXIF DateTimeOriginal'])
          orig = datetime.datetime.strptime(thething, '%Y:%m:%d %H:%M:%S')
          path = "%s\%s" %(dest,orig.date())
          if not os.path.exists(path):
            os.mkdir(path)

        for t in l:
            if t in tags.keys():
                vals[t] = str(tags[t])
            else:
                vals[t] = str(0)
            name = name + vals[t]
               
        n = hashlib.sha224(name.encode('utf-8')).hexdigest()
        new = path+'\\'+n+ext

        print("Old %s" %filepath)
        print("New %s" %new)

        if not os.path.isfile(new):


 
    
    