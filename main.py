

import turtle

t = turtle.Turtle()

number = []
number2 = []

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
    
buttonlayout()

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

while (True):
  numberchoice = input("Choose a number. Press enter to continue. ")
  print(numberchoice)
  try:
    res = (numberchoice)
    if (res == "1"):
      highlight(-90,140)
      number = number+[numberchoice]
    elif (res == "2"):
      highlight(-40,140)
      number = number+[numberchoice]
    elif (res == "3"):
      highlight(10,140)
      number = number+[numberchoice]
    elif (res == "4"):
      highlight(-90,90)
      number = number+[numberchoice]
    elif (res == "5"):
      highlight(-40,90)
      number = number+[numberchoice]
    elif (res == "6"):
      highlight(10,90)
      number = number+[numberchoice]
    elif (res == "7"):
      highlight(-90,40)
      number = number+[numberchoice]
    elif (res == "8"):
      highlight(-40,40)
      number = number+[numberchoice]
    elif (res == "9"):
      highlight(10,40)
      number = number+[numberchoice]
    elif (res == "0"):
      highlight(-40,-10)
      number = number+[numberchoice]
    elif (numberchoice == ""):
      break
    else:
      print("Try again. ")
  except:
    print("Error has occurred. ")
  
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
    elif (numberchoice2 == "2"):
      highlight(-40,140)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "3"):
      highlight(10,140)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "4"):
      highlight(-90,90)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "5"):
      highlight(-40,90)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "6"):
      highlight(10,90)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "7"):
      highlight(-90,40)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "8"):
      highlight(-40,40)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "9"):
      highlight(10,40)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == "0"):
      highlight(-40,-10)
      number2 = number2+[numberchoice2]
    elif (numberchoice2 == ""):
      break
    else:
      print("Try again. ")
  except:
    print("Error has occurred. ")