from math import*
from graphics import*
from time import*
def main():

    win = GraphWin("Travel Rectangle", 600, 450)
    win.setCoords(0,0,600,450)
    win.setBackground("White")

#circle, p1 = center, p2 = radius
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    cir = Circle(p1, p2.getX() - p1.getX())
    cir.draw(win)

#rectangle
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)

    rec = Rectangle(p3,p4)
    rec.setOutline("Red")
    rec.setFill("Red")
    rec.draw(win)

#center of rectangle
    x_center = (p3.getX() + p4.getX())/2
    y_center = (p3.getY() + p4.getY())/2
    rec_center = (x_center,y_center)

#initial theta
    
    initial_theta = atan((y_center - p1.getY())/(x_center - p1.getX()))
    theta = int(degrees(initial_theta))
    radius = cir.getRadius()

#travel
    win.getMouse()
    for i in range(10):
        for theta in range(theta, theta+360):
            a = radians(theta)
            dx = radius*cos(a) + p1.getX() - x_center
            dy = radius*sin(a) + p1.getY() - y_center
            rec.move(dx,dy)
            x_center = x_center+dx
            y_center = y_center+dy
            sleep(0.05)
            b = win.checkMouse()
            if (b == None):
                continue
            else:
                break
        if (b == None):
            continue
        else:
            break
    for j in range(5):
        for theta in range(theta, theta-360,-1):
            a = radians(theta)
            dx = radius*cos(a) + p1.getX() - x_center
            dy = radius*sin(a) + p1.getY() - y_center
            rec.move(dx,dy)
            x_center = dx+x_center
            y_center = dy+y_center
            sleep(0.05)         
           
main()
