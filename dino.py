import numpy as np
import cv2
import time
import pyautogui as p
import PIL as pi
import mss
def pro_image(img):
    final_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscale
    final_image = cv2.Canny(final_image, threshold1=200, threshold2=300) # edge detection
    return final_image

def main():
    while(True):
        with mss.mss() as sct:
            monitor = {"top": 577, "left": 340, "width": 63, "height": 60}
            img=sct.grab(monitor)
        img = np.array(img) # converts the image to an array
        final_image = pro_image(img)# sends the image to the function for futher processing

        m = np.mean(final_image) #finds the mean to determine if obstacle
        
        if not m == float(0): # checks if the mean is zero
            print(m) # prints the mean
            p.press('up') # presses the 'up' key
            time.sleep(0.078) # waits for some time (adjust this for more snappy landing)
            p.press('down')# presses the 'down' key

main()
