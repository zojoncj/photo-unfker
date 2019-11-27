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
        except Exception as e:
            print(e)
            continue
        tags = {}
        with open(filepath, 'rb') as f:
            try:
               tags = exifread.process_file(f, details=False)
            except:
                print("WTF:: %s" %filepath)
        vals = {}
        name = path = ""
        if "EXIF DateTimeOriginal" in tags.keys():
          thething = str(tags['EXIF DateTimeOriginal'])
          orig = datetime.datetime.strptime(thething, '%Y:%m:%d %H:%M:%S')
          ym = "%s-%s" %(orig.year,orig.month)
          path = "%s\%s" %(dest,ym)
          if not os.path.exists(path):
            os.mkdir(path)
        else:
            path=dest+'\\fucked'
            if not os.path.exists(path):
                os.mkdir(path)

        for t in l:
            if t in tags.keys():
                vals[t] = str(tags[t])
            else:
                vals[t] = str(0)
            name = name + vals[t]
               
        n = hashlib.md5(name.encode('utf-8')).hexdigest()
        new = path+'\\'+n+ext


        if not os.path.isfile(new):
            try:
                copyfile(filepath, new)
            except:
                print("WTF")
                print("Old %s" %filepath)
                print("New %s" %new)
                print(im)


 
    
    