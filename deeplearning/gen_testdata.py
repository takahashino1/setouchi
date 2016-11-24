#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

if __name__ == '__main__':
  outdir = sys.argv[1]

  if not os.path.isdir(outdir):
    sys.exit('%s is not directory' % outdir)

  names = {
    "good": 0,
    "bad": 1
  }

  #exts = ['.PNG','.JPG','.JPEG']
  exts = ['.JPG','.JPEG']

  for dirpath, dirnames, filenames in os.walk(outdir):
   for dirname in dirnames:
 #     print 'dirname=%s diranames =%s names=%s' % (dirname, dirnames,names)
      if dirname in names:
        n = names[dirname]
        member_dir = os.path.join(dirpath, dirname)
 
 #       print 'member_dir=%s' % (member_dir)

        for dirpath2, dirnames2, filenames2 in os.walk(member_dir):

 #         print 'dirpath2=%s dirname=%s' % (dirpath2,dirname)
 
          if not dirpath2.endswith(dirname):
            continue
          for filename2 in filenames2:

#            print 'filename2=%s filenames2=%s' % (filename2,filenames2) 

            (fn,ext) = os.path.splitext(filename2)
            if ext.upper() in exts:
              img_path = os.path.join(dirpath2, filename2)
              print '%s %s' % (img_path, n)

