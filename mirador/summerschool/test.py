#search for all jpg in subdir
#and save in list them with the name of the subdir
import os
import shutil
import sys
import re
import glob
import json
import requests
import time


def main():
    # get the current path
    current_path = os.getcwd()
    # get the list of all subdirectories
    subdirs = [x[0] for x in os.walk(current_path)]
    # remove the first element of the list
    # because it is the current path
    subdirs.pop(0)
    # create a list of all jpg files
    jpgs = []
    # loop through all subdirectories
    for subdir in subdirs:
        # get the list of all jpg files in the current subdir
        jpgs = glob.glob(subdir + '/*.jpg')
        # loop through all jpg files in the current subdir
        #esegui comando da shell

        for jpg in jpgs:
            os.exec("vips im_vips2tiff "+jpg+" "+jpg[:-4]+".tif:deflate,tile:256x256,pyramid")


if __name__ == '__main__':
    main()
