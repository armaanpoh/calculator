import turtle
import time

#80 is the limit of the x-value in the display

t = turtle.Turtle()
n = turtle.Turtle()

number = []
number2 = []
display = []

numvar = [-70,148]


def rectangle():
  for x in range(4):
    print (x)
    if (x == 0 or x == 2):
      move = 90
    else:
      move = 50
    t.forward(move)
    t.left(90)

def square():
    for x in range(4):
      t.forward(50)
      t.left(90)
t.penup()
#t.goto(-90,90)
t.pendown()
#rectangle()
def button(number):
  square()
  t.penup()
  t.forward(26)
  t.left(90)
  t.forward(12)
  t.pendown()
  t.write(number, align="center", font=("Arial", 14, "normal"))

def buttonlayout():
  for x in range(10):
    if x == 0:
      t.penup()
      t.goto(-40,-61)
      t.pendown()
    elif x == 1:
      t.penup()
      t.goto(-90,90)
      t.pendown()
    elif x == 4:
      t.penup()
      t.goto(-90,39)
      t.pendown()
    elif x == 7:
      t.penup()
      t.goto(-90,-12)
      t.pendown()
    button(x)
    t.penup()
    t.right(90)
    t.forward(24)
    t.right(90)
    t.forward(12)
    t.left(90)
    t.pendown()
    
#buttonlayout()

t.penup()
t.goto(80,90)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(106,103)
t.pendown()
t.write("+", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(80,40)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(106,53)
t.pendown()
t.write("-", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(80,-10)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(106,3)
t.pendown()
t.write("x", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(80,-60)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(106,-47)
t.pendown()
t.write("/", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(10,-61)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(36,-50)
t.pendown()
t.write("=", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(-90,-61)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(-64,-50)
t.pendown()
t.write("+/-", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(80,140)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(106,153)
t.pendown()
t.write(".", align="center", font=("Arial", 14, "normal"))

t.penup()
t.goto(-90,140)
t.pendown()
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)

def draw(numb):
  n.pendown
  n.color("black")
  n.write(numb, align="center", font=("Arial", 16, "normal"))
  n.penup()
  #print(numvar[0])
  numvar[0] += 15
  #print(numvar[0])

def highlight(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color("yellow")
  t.begin_fill()
  for x in range(4):
    t.forward(50)
    t.left(90)
  t.end_fill()
  time.sleep(0.2)
  for x in range(9):
    t.undo()
  n.penup()
  n.goto(numvar[0],148)

div = 9
    
while (True):
  numberchoice = input("Choose a number. Press enter to continue. ")
  print(numberchoice)
  try:
    for x in number:
      print(x)
    res = (numberchoice)
    if (res == "1"):
      highlight(-90,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display) < 9:
        display.append(numberchoice)
        print("Display array [0] value="+display[0])
        print("display length " + str(len(display)))
      # elif len(display) == 9:
      #   n.clear()
      #   display.pop()
      #   display.append(numberchoice)
      for x in range (20):
        if len(display) == x*9:
          n.clear()
          print("error found")
          n.goto(-70,148)
          numvar[0]=-70
          for x in display:
            draw(x)
            print("I made it")
          print("display length " + str(len(display))) 
      draw(1)

    """
    elif (res == "2"):
      highlight(-40,140)
      number = number+[numberchoice]
      draw(2)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "3"):
      highlight(10,140)
      number = number+[numberchoice]
      draw(3)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "4"):
      highlight(-90,90)
      t.penup()
      t.goto(numvar)
      number = number+[numberchoice]
      draw(4)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "5"):
      highlight(-40,90)
      number = number+[numberchoice]
      draw(5)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "6"):
      highlight(10,90)
      number = number+[numberchoice]
      draw(6)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "7"):
      highlight(-90,40)
      number = number+[numberchoice]
      draw(7)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "8"):
      highlight(-40,40)
      number = number+[numberchoice]
      draw(8)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "9"):
      highlight(10,40)
      number = number+[numberchoice]
      draw(9)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (res == "0"):
      highlight(-40,-10)
      number = number+[numberchoice]
      draw(0)
      if display.size < 9:
        display.append(numberchoice)
      elif display.size == 9:
        display.pop()
        display.append(numberchoice)
    elif (numberchoice == ""):
      break
    
    else:
      print("Try again. ")
      """
  except Exception as e:
    print("Error has occurred. ", e)

operator = input("Choose an operator. ")
if (operator == "+"):
  highlight(80,140)
elif (operator == "-"):
  highlight(80,90)
elif (operator == "x"):
  highlight(80,40)
elif (operator == "/"):
  highlight(80,-10)

while (True):
  numberchoice2 = input("Choose a second number. Press enter to continue. ")
  print(numberchoice2)
  try:
    res = (numberchoice2)
    if (numberchoice2 == "1"):
      highlight(-90,140)
      number2 = number2+[numberchoice2]
      draw(1)
    elif (numberchoice2 == "2"):
      highlight(-40,140)
      number2 = number2+[numberchoice2]
      draw(2)
    elif (numberchoice2 == "3"):
      highlight(10,140)
      number2 = number2+[numberchoice2]
      draw(3)
    elif (numberchoice2 == "4"):
      highlight(-90,90)
      number2 = number2+[numberchoice2]
      draw(4)
    elif (numberchoice2 == "5"):
      highlight(-40,90)
      number2 = number2+[numberchoice2]
      draw(5)
    elif (numberchoice2 == "6"):
      highlight(10,90)
      number2 = number2+[numberchoice2]
      draw(6)
    elif (numberchoice2 == "7"):
      highlight(-90,40)
      number2 = number2+[numberchoice2]
      draw(7)
    elif (numberchoice2 == "8"):
      highlight(-40,40)
      number2 = number2+[numberchoice2]
      draw(8)
    elif (numberchoice2 == "9"):
      highlight(10,40)
      number2 = number2+[numberchoice2]
      draw(9)
    elif (numberchoice2 == "0"):
      highlight(-40,-10)
      number2 = number2+[numberchoice2]
      draw(0)
    elif (numberchoice2 == ""):
      break
    else:
      print("Try again. ")
  except:
    print("Error has occurred. ")