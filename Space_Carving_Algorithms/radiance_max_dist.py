import cv2
import numpy as np
import math

#This method calculates the distance between each projected pixel's vector and the average
# vector of all the projected pixels in the color space. If one of these projected pixels deviates 
# beyond a certain threshold distance from the average vector, the correpondent voxel fails the 
#color consistency check: distance for each pixel = sqrt((R-mu(R))^2+(G-mu(G))^2+(B-mu(B))^2)
def consistency(col_set):
    
    #print("Color set: ", col_set)
    col_center = np.mean(col_set, axis = 0) #The average vector in the color space
    #print("Color mean ",col_center)

    normed_col_center = col_set - col_center
    #print("Normed color set: ",normed_col_center)

    distance = np.sum(np.multiply(normed_col_center, normed_col_center), axis=1) #np.multiply performs
                                                                                 #element wise multiplication
    #print("Distances from the mean: ",distance)

    max_distance = np.amax(distance)
    #print("Maximum distance: ", max_distance)

    if math.sqrt(max_distance) > 100: # Beethoven Head ==> 10 or 5
                                     # Bunny ==>
                                     # Bird ==>
                                     #Pig ==>
                                     #It is enough to only check the projected pixel with the maximum distance
        return [False, col_center]
    else:
        return [True, col_center]