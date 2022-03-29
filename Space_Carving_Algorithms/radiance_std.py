import cv2
import numpy as np
import math

#This method calculates the distance between each projected pixel's vector and the average
# vector of all the projected pixels in the color space. If one of these projected pixels deviates 
# beyond a certain threshold distance from the average vector, the correpondent voxel fails the 
#color consistency check: distance for each pixel = sqrt((R-mu(R))^2+(G-mu(G))^2+(B-mu(B))^2)
def consistency(col_set):
    
    col_center = np.mean(col_set,axis=0)
    #print("Color set: ", col_set)
    col_std = math.sqrt(np.sum(np.var(col_set, axis = 0))) 
    #Var(resultant_color) = Var(R) + Var(G) +Var(B), assuming an additive color model in the acquired RGB images
    #print("Color standard deviation ",col_std)


    if col_std >= 1.73: # The standard deviation value should be tested from 1.73 ==> color deviation of 1 on each channel (on a 0-255 scale)
                                                                      #to  17.32 ==> color deviation of 10 on each channel (on a 0-255 scale)
        return [False, col_center]
    else:
        return [True, col_center]