import turtle
import time
import math

#80 is the limit of the x-value in the display

t = turtle.Turtle()
n = turtle.Turtle()

full=False

number = []
number2 = []
display = []
numberNeg = False
numberNeg2 = False

numvar = [-70,148]
per = 0
neg = 0
neg2 = 0


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

def draw(numb):
  n.goto(numvar[0], numvar[1])
  n.pendown()
  n.color("black")
  n.write(numb, move=True, align="center", font=("Arial", 16, "normal"))
  n.penup()
  numvar[0] += 15

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
  try:
    res = (numberchoice)
    if (res == "1"):
      highlight(-90,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9: 
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(1) 

    elif (res == "2"):
      highlight(-40,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(2)      
      
    elif (res == "3"):
      highlight(10,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(3)
        
    elif (res == "4"):
      highlight(-90,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(4)
        
    elif (res == "5"):
      highlight(-40,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(5)
      
    elif (res == "6"):
      highlight(10,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(6)
        
    elif (res == "7"):
      highlight(-90,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(7)
        
    elif (res == "8"):
      highlight(-40,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(8)
        
    elif (res == "9"):
      highlight(10,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(9)
        
    elif (res == "0"):
      highlight(-40,-10)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(0)
        
    elif (res == "."):
      highlight(80,190)
      number = number+[numberchoice]
      if len(display)+per+neg < 9:
        display.append(numberchoice)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(".")
        
    elif (res == "-"):
      highlight(-90,-10)
      numberNeg = True
      if len(display)+per+neg < 9:
        display.insert(0,numberchoice)
        n.clear()
        n.penup()
        numvar[0],numvar[1] = -70,148
        for x in display:
          draw(x)
      if len(display)+per+neg == 9:
        display.pop(0)
        full=True
        n.clear()
        numvar[0],numvar[1] = -70,148
        draw("-")
        for x in display:
          draw(x)
        
    elif (numberchoice == ""):
      break
    
    else:
      print("Try again. ")
  except Exception as e:
    print("Error has occurred. ", e)

operator = input("Choose an operator. ")
if (operator == "+"):
  n.clear()
  numvar[0],numvar[1] = -70,148
  highlight(80,140)
elif (operator == "-"):
  n.clear()
  numvar[0],numvar[1] = -70,148
  highlight(80,90)
elif (operator == "x"):
  n.clear()
  numvar[0],numvar[1] = -70,148
  highlight(80,40)
elif (operator == "/"):
  n.clear()
  numvar[0],numvar[1] = -70,148
  highlight(80,-10)

display=[]
while (True):
  numberchoice2 = input("Choose a second number. Press enter to continue. ")
  try:
    res = (numberchoice2)
    if (numberchoice2 == "1"):
      highlight(-90,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
        print(display[0])
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(1)
    elif (numberchoice2 == "2"):
      highlight(-40,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(2)
    elif (numberchoice2 == "3"):
      highlight(10,140)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(3)
    elif (numberchoice2 == "4"):
      highlight(-90,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(4)
    elif (numberchoice2 == "5"):
      highlight(-40,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(5)
    elif (numberchoice2 == "6"):
      highlight(10,90)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(6)
    elif (numberchoice2 == "7"):
      highlight(-90,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x)
      if full==False:
        draw(7) 
    elif (numberchoice2 == "8"):
      highlight(-40,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(8)
    elif (numberchoice2 == "9"):
      highlight(10,40)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(9)
    elif (numberchoice2 == "0"):
      highlight(-40,-10)
      t.penup()
      t.goto(numvar[0],numvar[1])
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(0)
    elif (res == "."):
      highlight(80,190)
      number2 = number2+[numberchoice2]
      if len(display)+per+neg < 9:
        display.append(numberchoice2)
      if len(display)+per+neg == 9:
          display.pop(0)
          full=True
          n.clear()
          numvar[0],numvar[1] = -70,148
          for x in display:
            draw(x) 
      if full==False:
        draw(".")
    elif (res == "-"):
      highlight(-90,-10)
      numberNeg2 = True
      if len(display)+per+neg < 9:
        display.insert(0,numberchoice2)
        n.clear()
        numvar[0],numvar[1] = -70,148
        for x in display:
          draw(x)
      if len(display)+per+neg == 9:
        display.pop(0)
        full=True
        n.clear()
        numvar[0],numvar[1] = -70,148
        draw("-")
        for x in display:
          draw(x)
      
    elif (numberchoice2 == ""):
      break
      highlight(-40,40)
    else:
      print("Try again. ")
  except:
    print("Error has occurred. ")

final=0.0
ans=0.0
ans2=0.0
decimal = False
decimalAns = ''
decimalAns2 = ''
for x in number:
  if x == ".":
    decimal = True
for x in number2:
  if x == ".":
    decimal = True
for x in number:
  decimalAns += str(x)
  #if numberNeg == True:
  #  decimalAns*=-1
for x in number2:
  decimalAns2 += str(x)
  #if numberNeg2 == True:
  #  decimalAns2*=-1
if decimal == False:
  for x in range(1,len(number)):
    l = math.floor(math.log10(float(number[x])) + 1)
    ans = ans * math.pow(10,1)
    ans += float(number[x])
  for x in range(1,len(number2)):
    l = math.floor(math.log10(float(number2[x])) + 1)
    ans2 = ans2 * math.pow(10,1)
    ans2 += float(number2[x])
else:
  if numberNeg and numberNeg2:
    ans = float(decimalAns[0:])
    ans2 = float(decimalAns2[0:])
  elif numberNeg and not numberNeg2:
    ans = float(decimalAns[0:])
    #ans = float(decimalAns)
    ans2 = float(decimalAns2)
  elif numberNeg2 and not numberNeg:
    ans = float(decimalAns)
    ans2 = float(decimalAns2[0:])
if numberNeg:
  ans=ans*-1
if numberNeg2:
  ans2=ans2*-1
print(ans)
print(ans2)
if operator == "+":
  final = ans+ans2
elif operator == "-":
  final = ans-ans2
elif operator == "*":
  final = ans*ans2
elif operator == "/":
  final = ans/ans2
n.clear()
numvar[0],numvar[1] = -70,148
print(final)
final = str(final)
if numberNeg and numberNeg2 and decimal:
  for x in range(len(display)):
    draw(final[x])
elif numberNeg or numberNeg2 and decimal:
  for x in range(len(display)+3):
    draw(final[x])
elif numberNeg or numberNeg2:
  for x in range(len(display)+1):
    draw(final[x])
elif decimal:
  for x in range(len(display)-1):
    draw(final[x])
else:
  for x in range(len(display)):
    draw(final[x])
print(final)