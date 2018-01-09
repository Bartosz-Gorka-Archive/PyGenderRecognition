from PIL import Image
import numpy as np
from scipy import ndimage
import skimage.morphology as mp
from skimage.filters.edges import convolve
from skimage import color,measure
import colorsys as cs
from matplotlib import pylab as plt
from skimage import img_as_ubyte
from skimage import data
import os
from math import ceil
from subprocess import call


def listing_music():
    file_names = []
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".wav"):
            name = os.path.join(cwd, file)
            file_names.append(file)

    return file_names


def main():
    music = listing_music()
    for i in range(len(music)):
        print(music[i])
        call(['python3', 'inf127228.py', music[i]])

if __name__ == '__main__':
    main()
