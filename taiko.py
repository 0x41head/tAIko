import cv2
import numpy as np
from mss import mss
import time
import keyboard

def screen_record():
    last_time = time.time()
    with mss() as sct:
        monitor = {"top": 415, "left": 705, "width": 98, "height": 111}
        while True:
            screen = np.array(sct.grab(monitor))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB)
            maskred = cv2.inRange(screen,(10,25,90),(20,35,100))
            if cv2.countNonZero(maskred) > 0:
                keyboard.press('f')
                time.sleep(0.1)
                keyboard.release('f')
            else:
                maskblue = cv2.inRange(screen,(70,70,35),(80,80,45))
                if cv2.countNonZero(maskblue) > 0:
                    keyboard.press('d')
                    time.sleep(0.1)
                    keyboard.release('d')
                else:
                    maskyellow = cv2.inRange(screen,(0,71,95.3),(0,71,95.3))
                    while(cv2.countNonZero(maskyellow) > 0):
                        keyboard.press('f')
                        time.sleep(0.1)
                        keyboard.release('f')
                        time.sleep(0.1)
                        keyboard.press('d')
                        time.sleep(0.1)
                        keyboard.release('d')
                        screen = np.array(sct.grab(monitor))
                        screen = cv2.cvtColor(screen,cv2.COLOR_BGRA2RGB)
                        maskyellow = cv2.inRange(screen,(0,71,95.3),(0,71,95.3))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__=="__main__":
    screen_record()
