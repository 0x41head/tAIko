import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, D,F, ReleaseKey


def screen_record():
    last_time = time.time()
    k=0
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(705,415,803,526)))
        
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
        maskred = cv2.inRange(screen,(10,25,90),(20,35,100))
        if cv2.countNonZero(maskred) > 0:
            PressKey(F)
            time.sleep(0.1)
            ReleaseKey(F)
        else:
            maskblue = cv2.inRange(screen,(70,70,35),(80,80,45))
            if cv2.countNonZero(maskblue) > 0:
                
                PressKey(D)
                time.sleep(0.1)
                ReleaseKey(D)
            else:
                i=10
                maskyellow = cv2.inRange(screen,(0,71,95.3),(0,71,95.3))
                while(cv2.countNonZero(maskyellow) > 0):
                    while(i):
                        PressKey(F)
                        time.sleep(0.01)
                        ReleaseKey(F)
                        time.sleep(0.01)
                        PressKey(D)
                        time.sleep(0.01)
                        ReleaseKey(D)
                        i-=1
                        

                    
                    screen =  np.array(ImageGrab.grab(bbox=(705,415,803,526)))
                    screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
                    maskyellow = cv2.inRange(screen,(0,71,95.3),(0,71,95.3))
                    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__=="__main__":
    k=0
    screen_record()
