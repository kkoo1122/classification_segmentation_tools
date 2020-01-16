import cv2
import json
import numpy as np
 

from glob import glob

filepath = '/media/kevintsai/de7d8362-52f9-4447-864e-05c8a4b461b5/KevinsStuff/potato/label/'
filename = '2018_04_24 15_37_30_88.png'
#filepath = 'C:/Users/kkoo_/Documents/Python/Work/Datasets/CitySpace/gtFine/'
#filename = 'aachen_000000_000019_gtFine_color.png'


for n in glob(filepath+filename):
    img = cv2.imread(n)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
    _, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    datastore = {'imgHeight':img.shape[0],'imgWidth':img.shape[1]}
    

    
    obj = []
    for c in contours:
        info = {}
        x, y, w, h = cv2.boundingRect(c) # get rect bounding box
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), thickness=2)
        #boxes.append([x,y,x+w,y+h])
        #labels.append(1)
        info['label'] = 'potato'
        info['boxes'] = [x,y,x+w,y+h]
        obj.append(info)


    
    datastore.update({'object':obj})
    #print(datastore)	
    cv2.drawContours(img, contours, -1, (0,0,255), 2)
    cv2.imshow("contours", img)
    
    
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
    
    cv2.destroyAllWindows()
    
    with open(n[:-4]+'_polygons.json','w', encoding='utf-8') as f:
    	json.dump(datastore, f, ensure_ascii=False, indent=4)
