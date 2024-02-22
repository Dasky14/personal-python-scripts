from tkinter import *
import colorsys
import random
import time
import threading

def __init__(self, *args, **kwargs):
    self.protocol('WM_DELETE_WINDOW', self.close_app)

def close_app(self):
    self.destroy()

canvas_size = 300

window = Tk()
window.geometry(str(canvas_size + 5) + "x" + str(canvas_size + 5))
window.resizable(False, False)
window.title("Bubble sort")

c = Canvas(window, width = canvas_size, height = canvas_size)
c.pack()

objValues = []
objects = []

def GetColour (value):
    rgbColor = colorsys.hsv_to_rgb(value / canvas_size, 1, 1)
    hexColor = "#%02x%02x%02x" % (int(rgbColor[0] * 255), int(rgbColor[1] * 255), int(rgbColor[2] * 255))
    return hexColor

for i in range(canvas_size):
    objValues.append(i)
    obj = c.create_line(i, canvas_size, i, canvas_size - i, fill = GetColour(i))
    objects.append(obj)
random.shuffle(objValues)

for i in range(len(objects)):
    coord = c.coords(objects[i])
    coord[3] = canvas_size - objValues[i]
    c.coords(objects[i], coord)

def SortTheThing ():
    comparisonCount = 0
    highlight = 0
    sortedCount = 0
    while True:
        swapMade = False
        for i in range(len(objects) - 1 - sortedCount):
            comparisonCount += 1
            if CheckIfLarger(i, i + 1):
                SwapCanvasItems(i, i + 1)
                swapMade = True

        sortedCount += 1
        if not swapMade:
            break
    print(comparisonCount)

def SwapCanvasItems (i1Num, i2Num):
    i1coords = c.coords(objects[i1Num])
    i2coords = c.coords(objects[i2Num])
    i1coords[3], i2coords[3] = i2coords[3], i1coords[3]
    objValues[i1Num], objValues[i2Num] = objValues[i2Num], objValues[i1Num]
    c.itemconfig(objects[i1Num], fill = GetColour(objValues[i1Num]))
    c.itemconfig(objects[i2Num], fill = GetColour(objValues[i2Num]))
    c.coords(objects[i1Num], i1coords)
    c.coords(objects[i2Num], i2coords)

def CheckIfLarger (i1Num, i2Num):
    return True if objValues[i1Num] > objValues[i2Num] else False

threading.Thread(target = SortTheThing).start()
window.mainloop()