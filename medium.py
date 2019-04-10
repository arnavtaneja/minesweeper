import numpy as np
from PIL import ImageGrab
import cv2
import time
from PIL import Image
import cv2
import pyautogui
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

from pynput.mouse import Button, Controller

time.sleep(5)

size = 16

#pyautogui.moveTo((112+32*x),(520+32*x))
#pyautogui.press('space')

pyautogui.click(315,482)
timer=0
while(timer<10000):
    im = ImageGrab.grab(bbox=(80, 488, 1100, 1510))  # X1,Y1,X2,Y2
    im.save('screenshot123.png')
    #im.show()


    im = Image.open('screenshot123.png') # Can be many different formats.
    pix = im.load()

    # Creates a list containing 5 lists, each of 8 items, all set to 0
    w, h = size, size;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    flagtotal=0
    for x in range(0,size):
        for y in range(0,size):
           #  print(pix[(32+64*x),(32+64*y)]) # prints the tuple value of a pixel
            if pix[(32+64*x),(32+64*y)] == (0, 35, 245, 255):
                Matrix[y][x]=1
            elif pix[(32+64*x),(32+64*y)] == (61, 124, 42, 255):
                Matrix[y][x]=2
            elif pix[(32+64*x),(32+64*y)] == (235, 50, 35, 255):
                Matrix[y][x]=3
            elif pix[(32+64*x),(32+64*y)] == (0, 11, 118, 255):  #4
                Matrix[y][x]= 4
            elif pix[(32+64*x),(32+64*y)] == (94, 48, 44, 255): #flags
                Matrix[y][x]= 9
                flagtotal+=1
            else:
                #  print(pix[(32+64*x),(1+64*y)])
                if pix[(32+64*x),(1+64*y)] == (255, 255, 255, 255):  #unopened
                    Matrix[y][x]=0
                else:
                    Matrix[y][x] = -5                        #opened


     # pyautogui.click(55, 260)
    print(np.matrix(Matrix))

    mx = [-1,-1,-1,0,0,1,1,1]
    my = [-1,0,1,-1,1,-1,0,1]


    for x in range (0,size):
        for y in range (0,size):
            opens = 8
            flags=0
            if Matrix[x][y] < 0 or Matrix[x][y] >=9:
                continue
            for k in range(8):
                nx = x + mx[k]
                ny = y + my[k]

                if(nx > size-1 or ny > size-1 or nx < 0 or ny < 0):
                    opens -= 1
                    continue
                if(Matrix[nx][ny] != 0):
                    opens -= 1
                if(Matrix[nx][ny]==9):
                    flags +=1
            print(x,y,opens,flags, Matrix[x][y])


            if (flags != 0 and flags == Matrix[x][y] and opens != 0):
                pyautogui.moveTo((32*y+54),(260+32*x))
                pyautogui.press('space')
                break

            if (opens == Matrix[x][y]-flags):
                if( x+1 <= size-1 and y+1 <= size-1 and Matrix[x+1][y+1]==0):
                    pyautogui.click((32*(y+1)+54),(260+32*(x+1)), button='right')
                    Matrix[x+1][y+1]=9
                    break

                if( x+1 <= size-1 and Matrix[x+1][y]==0):
                    pyautogui.click((32*y+54),(260+32*(x+1)), button='right')
                    Matrix[x+1][y]=9
                    break

                if( x+1 <= size-1 and y-1 >= 0 and Matrix[x+1][y-1]==0):
                    pyautogui.click((32*(y-1)+54),(260+32*(x+1)), button='right')
                    Matrix[x+1][y-1]=9
                    break

                if( y+1 <= size-1 and Matrix[x][y+1]==0):
                    pyautogui.click((32*(y+1)+54),(260+32*(x)), button='right')
                    Matrix[x][y+1]=9
                    break

                if(y-1 >= 0 and Matrix[x][y-1]==0):
                    pyautogui.click((32*(y-1)+54),(260+32*x), button='right')
                    Matrix[x][y-1]=9
                    break

                if( x-1 >=0  and y-1 >= 0 and Matrix[x-1][y-1]==0):
                    pyautogui.click((32*(y-1)+54),(260+32*(x-1)), button='right')
                    Matrix[x-1][y-1]=9
                    break

                if( x-1 >=0  and y+1 <= size-1 and Matrix[x-1][y+1]==0):
                    pyautogui.click((32*(y+1)+54),(260+32*(x-1)), button='right')
                    Matrix[x-1][ y+1]=9
                    break

                if( x-1 >=0  and Matrix[x-1][y]==0):
                    pyautogui.click((32*(y)+54),(260+32*(x-1)), button='right')
                    Matrix[x-1][y]=9
                    break

    timer+=1
    if(flagtotal==40):
        break
