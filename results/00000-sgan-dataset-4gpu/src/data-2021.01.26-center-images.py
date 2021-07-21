# data-2021.01.26-center-images.py

# center images

# 2021.01.26 initial coding; burgreen

import os
import sys
import math

from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter

#--------------------------------------------
def get_files( src_path, grep='.', ext='.' ):
#--------------------------------------------
# grab all files with extension ext
    all_files = []
    for root, dirs, files in os.walk(src_path):
        # for debugging purposes
        # print( root )
        # print( dirs )
        # print( files )
        for f in files:
            if ext in f:
               if grep in f: all_files.append( root + '/' + f )
    return all_files

#--------------------------------------------
def save_image( im, cnt, file, dst_path ):
#--------------------------------------------

  f, e = os.path.splitext(file)
  x = f.split('/')
  y = x[1].split(' ')
  #file = os.path.join( dst_path, y[0]+'_'+str(cnt)+'.png' )
  file = os.path.join( dst_path, y[0]+'.png' )
  if not os.path.exists(dst_path): 
    print( 'os.makedirs(', dst_path, ')' )
    os.makedirs(dst_path)
  print( 'saving file: ', file )
  im.save( file, 'PNG' )

#--------------------------------------------
def get_aabb( im ):
#--------------------------------------------

  threshold = 220

  s = im.size

  i0 = 1e6; i1 = -1e6
  j0 = 0; j1 = 0

  for j in range(im.size[1]):
    cnt = 0
    for i in range(im.size[0]):
      c = im.getpixel((i,j))
      r = c[0]
      g = c[1]
      b = c[2]
      a = (r+g+b)/3
      if a < threshold: 
        cnt += 1
        if i < i0: i0 = i
        if i > i1: i1 = i
    if cnt > 0 and j0 == 0: j0 = j
    if cnt > 0 and j0 != 0: j1 = j

  return (i0,j0,i1,j1)

#--------------------------------------------
def main( data_dir ):
#--------------------------------------------

  # user defined parameters
  ext = 'png'
  white = (255,255,255,0)
  destination_path = 'out'

  files = get_files( data_dir, ext=ext )
  #print(files) # debug
  #sys.exit()

  if len(files) == 0: print(' - no file match')
  if len(files) == 0: sys.exit()

  cnt = -1
  for file in files:
    print('reading file:', file )
    im = Image.open(file)
    c_im = (im.size[0]//2, im.size[1]//2)
    #print(im.size,c_im)
    aabb = get_aabb( im )
    c_aabb = ( (aabb[0]+aabb[2])//2, (aabb[1]+aabb[3])//2 )
    #print(aabb,c_aabb)
    delta = (c_aabb[0]-c_im[0], c_aabb[1]-c_im[1])
    #print(delta)
    data = (1,0,delta[0], 0,1,delta[1])
    im = im.transform(im.size, Image.AFFINE, data, fill=1, fillcolor=white )
    #im.show()
    save_image( im, cnt, file, destination_path )
  
#----------------------------------------------------
if __name__ == '__main__':
#----------------------------------------------------

  if len(sys.argv) == 1: print('usage: python main.py data_dir')
  if len(sys.argv) == 1: exit()

  data_dir = 'undefined' 
  if len(sys.argv) > 1: data_dir = sys.argv[1]
    
  main( data_dir )
