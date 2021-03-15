 # \author Diego Queiroz
 # \copyright MIT License
 #
 # \brief Convert all images in images folder to grayscale
import os
from os import scandir, getcwd
from os.path import join
from PIL import Image

# Converts images from images folder to grayscale
pathtodir = os.path.join(os.getcwd() + '/img-original')
pathtodir2 = os.path.join(os.getcwd() + '/img-altered')

for filename in scandir(pathtodir):
    filepath = join(pathtodir, filename)
    # Opening in 'L' mode applies 8-bit grayscale conversion (with no alpha channel, 
    # use 'LA' for that)
    img = Image.open(filepath).convert('L')
    # Resizing image to be the same size, but with simplest resampling technique (1-NN pixel)
    # will cut the memory size a bit
    resized = img.resize(img.size, resample=1)
    # Saving smaller grayscale image
    savename = filename.name.split('.')
    resized.save(join(pathtodir2, savename[0]+'a.'+savename[1]))