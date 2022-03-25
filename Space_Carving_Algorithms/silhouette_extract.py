#This code is to read and return the silhouette images that separate the target objects from the
#background
import os
import cv2



#Method to read and return the silhouette images that are offered in the datasets
def get_mask(file):
    #Setting the path
    data_dir = os.path.expanduser('~')
    data_dir = data_dir + "/Downloads/DataSets/beethoven_data/silhouettes/"
    silhouette_file = data_dir + file.split('.')[0] + ".pgm"
    img = cv2.imread(silhouette_file)
    return img
