from math import*
from graphics import*
def main():
    
#gui
    win = GraphWin("Airline Reservation System", 600,400)
    win.setBackground("white")
    firsttext = Text(Point(50,25), "First Name: ")
    firsttext.draw(win)
    First = Entry(Point(150,25),10)
    First.setFill("white")
    First.draw(win)
    lasttext = Text(Point(50,75), "Last Name: ")
    lasttext.draw(win)
    Last = Entry(Point(150,75),10)
    Last.setFill("white")
    Last.draw(win)
    classtext = Text(Point(425,25), "Class: ")
    classtext.draw(win)
    Class = Entry(Point(500,25),10)
    Class.setFill("white")
    Class.draw(win)
    pricetext = Text(Point(425, 75), "Price: ")
    pricetext.draw(win)
    seattext = Text(Point(50,125), "Seat #: ")
    seattext.draw(win)
    reserve1 = Rectangle(Point(150,175), Point(250,150))
    reserve1.draw(win)
    reservetext = Text(Point(200,163), "Reserve")
    reservetext.draw(win)
    quit1 = Rectangle(Point(350,175), Point(450,150))
    quit1.draw(win)
    quittext  = Text(Point(400,163), "Quit")
    quittext.draw(win)

#info
    name = First.getText(), Last.getText()
    classF = "First Class"
    priceF = "Fare $3000"
    classB = "Business Class"
    priceB = "Fare $2000"
    classE = "Economy Class"
    priceE = "Fare $1000"
    seatnumbertext = Text(Point(100,125), " ")
    seatnumbertext.draw(win)
    boardingtext = Text(Point(300,225), " ")
    boardingtext.draw(win)
    pricetext = Text(Point(490, 75), " ")
    pricetext.draw(win)

#seats
    seating_chart = [0]*100
    Fclass = seating_chart[0:30]
    Bclass = seating_chart[30:50]
    Eclass = seating_chart[50:100]

#reservation/saving to text file
    while True:
        clk = win.getMouse()
        fileIn = open("pass.txt", 'w')
        if (150<clk.getX()<250 and 150<clk.getY()<175):
            class_name = Class.getText()
            if class_name == "F":
                try:
                    seatnumbertext.setText(Fclass.index(0)+1)
                    Fclass.index(0)
                    Fclass.remove(0)
                    Fclass.insert(Fclass.index(0),1)
                    name = First.getText(), Last.getText()
                    seat = 'Seat', Fclass.index(0)
                    boardingF = name, classF, seat, priceF
                    pricetext.setText(priceF)
                    boardingtext.setText(boardingF)
                    fileIn.write("Name" + " " + First.getText() + " " + Last.getText() + " " + "First Class" + " " + "Seat#" + str(Fclass.index(0)) + " " + priceF)
                    
                except ValueError:
                    boardingtext.setText("There are no seats left in first class, do you want to choose another class?")
                    yes1 = Rectangle(Point(200,250), Point(250,275))
                    yes1.draw(win)
                    yestext = Text(Point(225,263), "Yes")
                    yestext.draw(win)
                    no1 = Rectangle(Point(300,250), Point(350,275))
                    no1.draw(win)
                    notext = Text(Point(325,263), "No")
                    notext.draw(win)
                    clk1 = win.getMouse()
                    if (200<clk1.getX()<250 and 250<clk1.getY()<275):
                        Class.setText("")
                        boardingtext.setText("")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                    elif (300<clk1.getX()<350 and 250<clk1.getY()<275):
                        boardingtext.setText("We are booked.")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                        break
                            
            if class_name == "B":
                try:
                    seatnumbertext.setText(Bclass.index(0)+31)
                    Bclass.index(0)
                    Bclass.remove(0)
                    Bclass.insert(Bclass.index(0),1)
                    name = First.getText(), Last.getText()
                    seat = 'Seat', Bclass.index(0)+30
                    boardingB = name, classB, seat, priceB
                    pricetext.setText(priceB)
                    boardingtext.setText(boardingB)
                    fileIn.write("Name" + " " + First.getText() + " " + Last.getText() + " " + "Business Class" + " " + "Seat#" + str(Bclass.index(0)+30) + " " + priceB)
                    
                except ValueError:
                    boardingtext.setText("There are no seats left in the business class, do you want to choose another class?")
                    yes1 = Rectangle(Point(200,250), Point(250,275))
                    yes1.draw(win)
                    yestext = Text(Point(225,263), "Yes")
                    yestext.draw(win)
                    no1 = Rectangle(Point(300,250), Point(350,275))
                    no1.draw(win)
                    notext = Text(Point(325,263), "No")
                    notext.draw(win)
                    clk1 = win.getMouse()
                    if (200<clk1.getX()<250 and 250<clk1.getY()<275):
                        Class.setText("")
                        boardingtext.setText("")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                    elif (300<clk1.getX()<350 and 250<clk1.getY()<275):
                        boardingtext.setText("We are booked.")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                        break

            if class_name == "E":
                try:
                    seatnumbertext.setText(Eclass.index(0)+51)
                    Eclass.index(0)
                    Eclass.remove(0)
                    Eclass.insert(Eclass.index(0),1)
                    name = First.getText(), Last.getText()
                    seat = 'Seat', Eclass.index(0)+50
                    boardingE = name, classE, seat, priceE
                    pricetext.setText(priceE)
                    boardingtext.setText(boardingE)
                    fileIn.write("Name" + " " + First.getText() + " " + Last.getText() + " " + "Economy Class" + " " + "Seat#" + str(Eclass.index(0)+50) + " " + priceE)
                    
                except ValueError:
                    boardingtext.setText("There are no seats left in the economy class, do you want to choose another class?")
                    yes1 = Rectangle(Point(200,250), Point(250,275))
                    yes1.draw(win)
                    yestext = Text(Point(225,263), "Yes")
                    yestext.draw(win)
                    no1 = Rectangle(Point(300,250), Point(350,275))
                    no1.draw(win)
                    notext = Text(Point(325,263), "No")
                    notext.draw(win)
                    clk1 = win.getMouse()
                    if (200<clk1.getX()<250 and 250<clk1.getY()<275):
                        Class.setText("")
                        boardingtext.setText("")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                    elif (300<clk1.getX()<350 and 250<clk1.getY()<275):
                        boardingtext.setText("We are booked.")
                        yestext.setText("")
                        notext.setText("")
                        yes1.undraw()
                        no1.undraw()
                        break
        elif (350<clk.getX()<450 and 150<clk.getY()<175):                    
            win.close()
        fileIn.close()
                
main()
