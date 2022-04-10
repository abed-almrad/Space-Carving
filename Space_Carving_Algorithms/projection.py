import os
import cv2
import numpy as np


# Method to extract the camera calibration matrices that have been already provided in
# the datasets
def projectionMatrix(file):
    # Setting the path
    data_dir = os.path.expanduser('~')
    data_dir = data_dir + "/Downloads/DataSets/statue_head_data/calib/"
    
    projection_file_name = data_dir + file.split('.')[0] + ".txt"
    proj_file = open(projection_file_name, "r+")
    matrix_line = proj_file.readline()
    P = np.empty((3,4), dtype = float)
    for i in range(3):
        matrix_line = proj_file.readline()
        for j in range(4):
            P[i, j] = float(matrix_line.split()[j])
    return P