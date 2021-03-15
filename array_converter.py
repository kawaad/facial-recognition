 # \author Diego Queiroz
 # \copyright MIT License
 #
 # \brief Convert all grayscale images in images folder to numpy arrays
import os
import numpy as np
from PIL import Image

def array_converter(w,d):
    # Converts grayscale images to 1-D float arrays.
    pathtodir = os.path.join(os.getcwd() + '/img-altered')
    listfaces = []
    listnames = []
    for filename in os.scandir(pathtodir):
        img = Image.open(os.path.join(pathtodir, filename))
        s = filename.name.split('_')[0]
        listnames.append(s)
        # Convert grayscale imgs to numpy flat array (1-D)
        imgdata = np.asarray(img).flatten()
        listfaces.append(imgdata)
    target = np.array(listnames)
    faces = np.array(listfaces)
    # Converting to float for ML models and standardizing
    faces = np.float32(faces)
    # Standardizing data
    faces = faces - faces.min()
    faces /= faces.max()
    faces = faces.reshape((faces.shape[0], w, d))
    faces_vectorized = faces.reshape(len(faces), -1)
    return faces_vectorized, target
