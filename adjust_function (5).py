from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import misc
from pylab import *



def imadjust(f, low_in, high_in, low_out, high_out, gamma = 1):
    
    f = f/225.0
    w, h = f.shape
    f1 = np.zeros((w, h),dtype=np.float64)
    # imadjust函数运算部分
    for x in range(0, w):
        for y in range(0, h):
            if f[x, y] <= low_in:
                f1[x, y] = low_out
            elif f[x, y] >= high_in:
                f1[x, y] = high_out
            elif high_in-low_in==0:
                f1[x,y] =0
            else:
                
                #c = 1
                #f1[x, y] = c * (f[x, y]**gamma)
                f1[x,y] = ((high_out-low_out)/(high_in-low_in))*(f[x,y]-low_in)**gamma + low_out
    
    
    #plt.figure(3)
    f2 = np.abs(f-f1)     #差值的绝对值
    
    return f1


def image_process(im_black, img_class):

    weights1={'wrist':[0.35,0.55],'shoulder':[0.2,0.5], 'humerus':[0.2,0.5],'hand':[0.2,0.4],'forearm':[0.2,0.4],'finger':[0.1,0.55],'elbow':[0.1,0.3]}
    weights2={'wrist':0.35,'shoulder':0.2, 'humerus':0.2,'hand':0.2,'forearm':0.2,'finger':0.1,'elbow':0.1}
    #{'wrist':0.84,'shoulders':0.85,'humerus':0.89,'hand':0.93,'forearm':0.8,'figure':0.78,'elbow':0.8}
    if img_class == 'wrist':
        low_in = 0.2
        high_in = 0.6
        param2 = 0.25
        UPP = 0.84
    elif img_class == 'shoulder':
        low_in = 0.14
        high_in = 0.4
        param2 = 0.3
        UPP = 0.85
    elif img_class == 'humerus':
        low_in = 0.1
        high_in = 0.4
        param2 = 0.25
        UPP = 0.89
    elif img_class == 'hand':
        low_in = 0.1
        high_in = 0.3
        param2 = 0.15
        UPP = 0.93
    elif img_class == 'forearm':
        low_in = 0.1
        high_in = 0.6
        param2 = 0.25
        UPP = 0.8
    elif img_class == 'finger':
        low_in = 0.1
        high_in = 0.66
        param2 = 0.1
        UPP = 0.78
    elif img_class == 'elbow':
        low_in = 0.2
        high_in = 0.4
        param2 = 0.15
        UPP = 0.8
        
    low_out=0
    high_out=1
    
    
    beta = 0.5 - 0.5*np.sqrt(4*UPP-3)
    l,w = im_black.shape
    im_black3 = np.zeros((l,w))
    for i in range(0,l):
        for j in range(0,w):
            im_black3[i,j] = min(beta,im_black[i,j]) + (max(im_black[i,j]-beta,0))**2
    
    
    im_black = im_black3*255.0
    
    
    #im_black = imadjust(im_black,0.1,0.3,0,1)
    im_black = imadjust(im_black,low_in,high_in,low_out,high_out)
    # 10, 15, 80, 85, 75, 75
    #im_black = normalize(im_black)
#     plt.imshow(im_black, cmap='gray')
#     plt.axis('off')
#     plt.show()
    for i in range(0,224):
        for j in range(0,224):
            if im_black[i,j] > param2:
                im_black[i,j] = 1
            else:
                im_black[i,j] = 0
                
    return im_black

