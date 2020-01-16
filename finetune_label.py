import cv2
import matplotlib.pyplot as plt
import numpy as np

from glob import glob

from IPython import embed


for filename in glob('./train/*.png'):
    print(filename[7:])
    img = cv2.imread(filename)    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    
    _, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    img_gray = gray
    #img_gray = np.expand_dims(gray, 2)
    #cv2.drawContours(img, contours, -1, (0,0,255), 2)
    for i in range(len(contours)):
        cv2.fillPoly(img_gray, pts=[contours[i]], color=[i+101])
    
    #plt.imshow(img_gray)
    #plt.show()
    #cv2.imshow('label',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    filnames_new = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/images_new/gtFine'+filename[1:]
    cv2.imwrite(filnames_new, img_gray)
    
    """
    newlabel = cv2.imread(filnames_new)
    newlabel = cv2.cvtColor(newlabel,cv2.COLOR_BGR2GRAY)
    newlabel = newlabel.astype(np.float)
    #newlabel[:,:,[0,1,2]] = newlabel[:,:,[2,1,0]]
    #newlabel = newlabel/255.
    plt.imshow(newlabel)
    plt.show()
    """
    
embed()
