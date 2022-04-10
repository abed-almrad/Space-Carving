import cv2
import numpy as np
import math

#This method calculates standard deviation of the RGB additive color model for the projection pixels and compares it to
#a threshold value
def consistency(col_set,threshold):
    
    col_center = np.mean(col_set,axis=0)
    #print("Color set: ", col_set)
    col_std = math.sqrt(np.sum(np.var(col_set, axis = 0))) 
    #Var(resultant_color) = Var(R) + Var(G) +Var(B), assuming an additive color model in the acquired RGB images
    #print("Color standard deviation ",col_std)


    if col_std >= threshold: # The standard deviation value should be tested from 1.73 ==> color deviation of 1 on each channel (on a 0-255 scale)
                                                                      #to  17.32 ==> color deviation of 10 on each channel (on a 0-255 scale)
        return [False, col_center]
    else:
        return [True, col_center]