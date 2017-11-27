from graphics import*
from time import*
def main():
    a = GraphWin("Traffic Lights", 600, 450)
    a.setCoords(0, 0, 500, 500)
    a.setBackground("White")
    M = Text(Point(180, 480), "Traffic Lights")
    M.setTextColor("forest green")
    M.draw(a)
    
#buttons
    p1 = Point(50, 100)
    p2 = Point(150, 150)
    rec1 = Rectangle(p1,p2)
    rec1.setOutline("forest green")
    rec1.draw(a)
    M1 = Text(Point(100,125), "Start")
    M1.setTextColor("forest green")
    M1.draw(a)

    p3 = Point(200, 100)
    p4 = Point(300, 150)
    rec2 = Rectangle(p3, p4)
    rec2.setOutline("forest green")
    rec2.draw(a)
    M2 = Text(Point(250,125), "Quit")
    M2.setTextColor("forest green")
    M2.draw(a)
    
#code for inputs:
    M3 = Text(Point(450,420), "Enter Red Time")
    M3.setTextColor("forest green")
    M3.draw(a)
    inputRed = Entry(Point(450,400), 10)
    inputRed.draw(a)
    inputRed.setText(0)
    inputRed.setFill("white")
    g1 = inputRed.getText()   

    M4 = Text(Point(450,370), "Enter Green Time")
    M4.setTextColor("forest green")
    M4.draw(a)
    inputGreen = Entry(Point(450,350), 10)
    inputGreen.draw(a)
    inputGreen.setText(0)
    inputGreen.setFill("white")
    g2 = inputGreen.getText()

    M5 = Text(Point(450,320), "Enter Yellow Time")
    M5.setTextColor("forest green")
    M5.draw(a)
    inputYellow = Entry(Point(450,300), 10)
    inputYellow.draw(a)
    inputYellow.setText(0)
    inputYellow.setFill("white")
    g3 = inputYellow.getText()

    M6 = Text(Point(450,270), "Enter Pedestrian")
    M6.setTextColor("forest green")
    M6.draw(a)
    inputPed = Entry(Point(450,250), 10)
    inputPed.draw(a)
    inputPed.setText(0)
    inputPed.setFill("white")
    g4 = inputPed.getText()
  
#code for traffic lights:
    M7 = Text(Point(100,200),"Street A")
    M7.setTextColor("forest green")
    M7.draw(a)
    
    M8 = Text(Point(250,200),"Street B")
    M8.setTextColor("forest green")
    M8.draw(a)
    
    p5 = a.getMouse()
    p5.draw(a)
    p6 = a.getMouse()
    p6.draw(a)
    rec3 = Rectangle(p5, p6)
    rec3.draw(a)
    
    p7 = a.getMouse()
    cir1 = Circle(p7, 20)
    cir1.setOutline("Red")
    cir1.draw(a)
    
    p8 = a.getMouse()
    cir2 = Circle(p8, 20)
    cir2.setOutline("Yellow")
    cir2.draw(a)
    
    p9 = a.getMouse()
    cir3 = Circle(p9, 20)
    cir3.setOutline("Green")
    cir3.draw(a)
    
    p10 = a.getMouse()
    p10.draw(a)
    p11 = a.getMouse()
    p11.draw(a)
    rec4 = Rectangle(p10, p11)
    rec4.draw(a)
    
    p12 = a.getMouse()
    cir4 = Circle(p12, 20)
    cir4.setOutline("Red")
    cir4.draw(a)
    
    p13 = a.getMouse()
    cir5 = Circle(p13, 20)
    cir5.setOutline("Yellow")
    cir5.draw(a)
    
    p14 = a.getMouse()
    cir6 = Circle(p14, 20)
    cir6.setOutline("Green")
    cir6.draw(a)

#code for evaluating buttons
    p15 = a.getMouse()
    p16 = a.getMouse()
    if(p16.getX() > p3.getX() and p16.getX() < p4.getX() and p16.getY() > p3.getY() and p16.getY() < p4.getY()):
        quit()
    else:
        if(p15.getX() > p1.getX() and p15.getX() < p2.getX() and p15.getY() > p1.getY() and p15.getY() < p2.getY()):
            while True:
                
                g1 = inputRed.getText()
                g2 = inputGreen.getText()
                g3 = inputYellow.getText()
                g4 = inputPed.getText()
                
                if(int(g4) == 1):
                    
                    cir1.setFill("red")
                    cir4.setFill("red")
                    sleep(int(g1))
                    sleep(int(g1))
                    cir1.setFill("white")
                    cir4.setFill("white")

                cir1.setFill("red")
                cir6.setFill("green")
                sleep(int(g1))
                sleep(int(g2))
                cir1.setFill("white")
                cir6.setFill("white")
                    
                cir2.setFill("yellow")
                cir5.setFill("yellow")
                sleep(int(g3))
                sleep(int(g3))
                cir2.setFill("white")
                cir5.setFill("white")
                    
                cir3.setFill("green")
                cir4.setFill("red")
                sleep(int(g2))
                sleep(int(g1))
                cir3.setFill("white")
                cir4.setFill("white")
                    
                cir2.setFill("yellow")
                cir5.setFill("yellow")
                sleep(int(g3))
                sleep(int(g3))
                cir2.setFill("white")
                cir5.setFill("white")
    
main()
