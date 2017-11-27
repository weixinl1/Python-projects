from graphics import *
from math import *
def main():
    win = GraphWin("Caesar cipher", 600, 450)
    win.setCoords(0,0,500,500)

#text
    L1 = Text(Point(100,450), "Please enter the text file name")
    L1.setTextColor("blue")
    L1.draw(win)
    L2 = Text(Point(120, 350), "Steps:")
    L2.draw(win)
    inputsteps = Entry(Point(250,350), 25)
    inputsteps.color = "black"
    inputsteps.fill = "white"
    inputsteps.draw(win)
    L3 = Text(Point(120, 400), "File Name:")
    L3.draw(win)
    inputfile = Entry(Point(250,400),25)
    inputfile.color = "black"
    inputfile.fill = "white"
    inputfile.draw(win)
    L4 = Text(Point(150, 200), "Original message")
    L4.draw(win)
    L5 = Text(Point(300, 200), "Encrypted message")
    L5.draw(win)

#open button
    p1 = Point(360, 420)
    p2 = Point(420, 380)
    openbox = Rectangle(p1,p2)
    openbox.draw(win)
    opentext = Text(Point(390, 400), "Open")
    opentext.draw(win)
    
#encode button
    p3 = Point(360, 370)
    p4 = Point(420, 330)
    encodebox = Rectangle(p3,p4)
    encodebox.draw(win)
    encodetext = Text(Point(390, 350), "Encode")
    encodetext.draw(win)

#save button
    p5 = Point(430, 370)
    p6 = Point(490, 330)
    savebox = Rectangle(p5,p6)
    savebox.draw(win)
    savetext = Text(Point(460,350), "Save")
    savetext.draw(win)

#quit button
    p7 = Point(360, 50)
    p8 = Point(420, 90)
    quitbox = Rectangle(p7,p8)
    quitbox.setOutline("red")
    quitbox.draw(win)
    quittext = Text(Point(390,70), "Quit")
    quittext.setTextColor("red")
    quittext.draw(win)
    
#open function   
    clk1 = win.getMouse()
    if (clk1.getX() > p1.getX() and clk1.getX() < p2.getX() and clk1.getY() < p1.getY() and clk1.getY() > p2.getY()):
        fname = inputfile.getText()
        fileIn = open(fname, 'r')
        if fileIn != None:
            for i in range(2):
                content = fileIn.readline()
                content.strip()
                content1 = Text(Point(150,150-5*i), content)
                content1.draw(win)
        fileIn.close()

#encode function
    clk2 = win.getMouse()
    if (clk2.getX() > p3.getX() and clk2.getX() < p4.getX() and clk2.getY() < p3.getY() and clk2.getY() > p4.getY()):
        steps = int(inputsteps.getText())    
        fname = inputfile.getText()
        fileIn = open(fname, 'r')
        if fileIn != None:
            for i in range(2):
                content = fileIn.readline()
                for word in content.split("\n"):
                    newcontent = ''
                    for letter in word :
                        encoded_ascii = ord(letter) - steps
                        if(steps > 26):
                            steps %= 26
                        if(encoded_ascii) < ord('A'):
                            encoded_ascii += 26
                        if(encoded_ascii) == 33:
                            encoded_ascii = 32
                        newcontent = newcontent + chr(encoded_ascii)
                        content1 = ' '.join(newcontent).strip(" ")
                        encrypt = content1.replace(" ",' ')
                    encoded1 = Text(Point(300,160-15*i), newcontent)
                    encoded1.draw(win)
        fileIn.close()

#save/quit function
    clk3 = win.getMouse()
    if (clk3.getX() > p5.getX() and clk3.getX() < p6.getX() and clk3.getY() < p5.getY() and clk3.getY() > p6.getY()):
        fileOut = open("out.txt", 'w')
        steps = int(inputsteps.getText())    
        fname = inputfile.getText()
        fileIn = open(fname, 'r')
        if fileIn != None:
            for i in range(2):
                content = fileIn.readline()
                for word in content.split("\n"):
                    newcontent = ''
                    for letter in word :
                        encoded_ascii = ord(letter) - steps
                        if(steps > 26):
                            steps %= 26
                        if(encoded_ascii) < ord('A'):
                            encoded_ascii += 26
                        if(encoded_ascii) == 33:
                            encoded_ascii = 32
                        newcontent = newcontent + chr(encoded_ascii)
                    fileOut.write(newcontent + '\n')
        fileIn.close()
        fileOut.close()
    elif (clk3.getX() > p7.getX() and clk3.getX() < p8.getX() and clk3.getY() > p7.getY() and clk3.getY() < p8.getY()):
        fileOut = open("out.txt", 'w')
        steps = int(inputsteps.getText())    
        fname = inputfile.getText()
        fileIn = open(fname, 'r')
        if fileIn != None:
            for i in range(2):
                content = fileIn.readline()
                for word in content.split("\n"):
                    newcontent = ''
                    for letter in word :
                        encoded_ascii = ord(letter) - steps
                        if(steps > 26):
                            steps %= 26
                        if(encoded_ascii) < ord('A'):
                            encoded_ascii += 26
                        if(encoded_ascii) == 33:
                            encoded_ascii = 32
                        newcontent = newcontent + chr(encoded_ascii)
                    fileOut.write(newcontent + '\n')
        fileIn.close()
        fileOut.close()
        quit()

#quit only function
    clk4 = win.getMouse()
    if (clk4.getX() > p7.getX() and clk4.getX() < p8.getX() and clk4.getY() > p7.getY() and clk4.getY() < p8.getY()):
        fileOut = open("out.txt", 'w')
        steps = int(inputsteps.getText())    
        fname = inputfile.getText()
        fileIn = open(fname, 'r')
        if fileIn != None:
            for i in range(2):
                content = fileIn.readline()
                for word in content.split("\n"):
                    newcontent = ''
                    for letter in word :
                        encoded_ascii = ord(letter) - steps
                        if(steps > 26):
                            steps %= 26
                        if(encoded_ascii) < ord('A'):
                            encoded_ascii += 26
                        if(encoded_ascii) == 33:
                            encoded_ascii = 32
                        newcontent = newcontent + chr(encoded_ascii)
                    fileOut.write(newcontent + '\n')
        fileIn.close()
        fileOut.close()
        quit()
    
        


main()
    
