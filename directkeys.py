from inputs import get_key
import time

def press_key(key):
    get_key(key)
    time.sleep(1)

def release_key(key):
    get_key(key)
    time.sleep(1)

if __name__ == '__main__':
    press_key('X')
    release_key('X')
