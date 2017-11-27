from graphics import*
def main():
    win = GraphWin("Olympic Flag", 600, 450)
    win.setCoords(0, 0, 60, 45)
    win.setBackground("white")

    #code to make rectangle
    p = Point(20,15)
    L = Text(p, "Click two places for a rectangle")
    L.draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    Rec = Rectangle(p1,p2)
    Rec.draw(win)

    #code to make circles
    L.setText("Click five places for center of the circles")
    
    p3 = win.getMouse()
    p4 = win.getMouse()
    p5 = win.getMouse()
    p6 = win.getMouse()
    p7 = win.getMouse()

    c1 = Circle(p3, 4)
    c2 = Circle(p4, 4)
    c3 = Circle(p5, 4)
    c4 = Circle(p6, 4)
    c5 = Circle(p7, 4)

    c1.draw(win)
    c1.setOutline("blue")
    c1.setWidth(3)
    
    c2.draw(win)
    c2.setOutline("yellow")
    c2.setWidth(3)
    
    c3.draw(win)
    c3.setOutline("black")
    c3.setWidth(3)
    
    c4.draw(win)
    c4.setOutline("green")
    c4.setWidth(3)
    
    c5.draw(win)
    c5.setOutline("red")
    c5.setWidth(3)
    
    #code to show where user clicked:
    p3.draw(win)
    p4.draw(win)
    p5.draw(win)
    p6.draw(win)
    p7.draw(win)

main()
    
    
    
    
