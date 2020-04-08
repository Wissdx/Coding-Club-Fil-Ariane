from tkinter import *


incr = 2
size = incr * 10
posX = 1
posY = 1
map = [[]] * 100

for value in range(0, 100):
    map[value] = [0] * 100



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x * (incr), 0, x * (incr), canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y * (incr), canvas_width, y * (incr), fill="#476042")

def right(x):
    global posX
    global posY
    if (map[posY][posX + 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX += x
    
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def left(x):
    global posX
    global posY
    if (map[posY][posX - 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX -= x
    
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def up(x):
    global posY
    global posX
    if (map[posY - 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY -= x

    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def down(x):
    global posY
    global posX
    if (map[posY + 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY += x
    
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)



dir = []

def algo(value):
    if map[posX][posY] != 1 and map[posX+1][posY] != -1 or map[posX-1][posY] != -1 and map[posX][posY+1] or map[posX][posY-1]:
        down(2)
        right(3)
        down(2)
        left(2)
        down(4)
        right(5)
        down(2)
        left(2)
        down(4)
        right(3)
        up(2)
        right(17)
        up(2)
        left(3)
        up(2)
        left(2)
        up(2)
        right(11)
        down(4)
        right(13)
        down(6)
        left(6)
        down(2)
        right(9)
        down(2)
        
        
        
def setACaseXY(X, Y, color):
    points = [X * size, Y * size, size * (X + 1), Y * size, size * (X + 1), size * (Y + 1), X * size, size * (Y + 1)]
    w.create_polygon(points, outline="#476042", fill=color, width=4)



master = Tk()
master.title("Ez le labyrinthe de ses morts")
master.iconbitmap("siphano.ico")
canvas_width = 1000
canvas_height = 1000
w = Canvas(master,width=1000,height=1000)



path = 'map.txt'
with open(path) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       x = line.find('x')
       while x != -1:
           setACaseXY(x, cnt, 'red')
           map[cnt][x] = 1
           x = line.find('x', x + 1)
       line = fp.readline()
       cnt += 1

w.pack()

#setACaseXY(47, 21, 'green')
#map[21][47] = 2


for value in range(0, 1000):
    master.after(value * 100000, algo, value)

checkered(w,10)

mainloop()
