import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y

# You then need to bind that function to a window that will capture the mouse click
def getPos(img):

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    # then, in a infinite processing loop (or whatever you want)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27: #click on escape to escape, genius
            break
        elif k == ord('a'): #click on 'a' to get value
            try:
                print mouseX,mouseY
            except NameError:
                print 'click first dumbass'

    cv2.destroyAllWindows()
    return mouseX, mouseY, img[mouseX, mouseY]

if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    getPos(img)