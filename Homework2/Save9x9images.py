import os
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw
from PIL import Image



img = Image.new('RGB', (25, 25), color = (255,215,0))
img.save('goal.jpg')

def goog():

    border_value = (80, 80, 80)

    img = cv2.imread(r"C:\Users\Win10\Deep-Reinforcement-Learning-uos\Homework2\img\goal.jpg")
    outterborder = img.shape[0]

    img[0, :] = border_value
    img[:,0] = border_value
    img[outterborder-1,:] = border_value
    img[:,outterborder - 1] = border_value

    cv2.imwrite(r"C:\Users\Win10\Deep-Reinforcement-Learning-uos\Homework2\Tile Images\goal.jpg",img)


def doStufF():
    for file in os.listdir(r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images"):
        img = cv2.imread(os.path.join(r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images",file))

        ##outterborder = img.shape[0]

        border_value = (255,0,0)

        ##x_start = 6

        x_middle = 12
        x_start = 6
        x_end = 19

        y_start = 6
        y_middle = 12 #6
        ##y_middle_middle = y_middle - 4
        y_end = 20



        shape_points = [[(6, 20), (19, 20), (12, 9)]]

        """img[y_middle:y_end,x_middle] = border_value # strich unten 
        img[y_end+2,x_middle] = border_value # fragezeichen punkt
        img[y_middle_middle,x_end] = border_value # rechter aussenpunkt
        img[y_middle_middle,x_start] = border_value # linker aussenpunkt
        img[y_start,x_middle] = border_value # oberer punkt"""

        #cv2.line(img,pt1=(x_start,y_end),pt2=(x_end,y_end),color=border_value,thickness=2) # strich unten links nach rechts
        #cv2.line(img,pt1=(x_start,y_end),pt2=(x_middle,y_middle),color=border_value,thickness=2) # strich unten links mitte
        #cv2.line(img,pt1=(x_end,y_end),pt2=(x_middle,y_middle),color=border_value,thickness=2) # strich unten rechts mitte
        ##cv2.line(img,pt1=(x_start,y_middle_middle),pt2=(x_middle,y_start),color=border_value,thickness=2) # strich rechts nach oben

        ##cv2.line(img,pt1=(x_middle,y_end+2),pt2=(x_middle,y_end+3),color=border_value,thickness=2) # punkt """
        #cv2.polylines(img, np.array(shape_points), True, border_value, 0) #dreieck
        #cv2.fillPoly(img, np.array(shape_points), border_value) #fill
        cv2.circle(img, (x_middle, y_middle), 3, border_value, 2) # kreis

        cv2.imwrite(os.path.join(r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images",file[:-4]+"_trace.jpg"),img)

doStufF()