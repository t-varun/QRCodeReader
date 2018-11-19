import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data.decode('UTF-8'),'\n')     
        text = obj.data.decode('UTF-8')
        #cap.release()
        #cv2.destroyAllWindows()
    return decodedObjects

def Draw():
    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
        # Number of points in the convex hull
        n = len(hull)     
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)
    return 

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decodedObjects = decode(im)
    Draw()              
    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'): # wait for 's' key to save 
        cv2.imwrite('Capture.png', frame)     

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
