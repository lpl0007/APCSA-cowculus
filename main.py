# L. Louque
# 1/12/2023-1/15/2023
# cowculus

import turtle

t = turtle.Turtle()

def drawBell():
  #Leather
  t.up()
  t.width(1)
  t.setpos(xValue+120,yValue+220)
  t.color(leatherColor)
  t.seth(-60)
  t.down()
  t.begin_fill()
  t.circle(-140,125)
  t.left(140)
  print(t.pos())
  t.forward(50)
  t.left(50)
  t.circle(155,120)
  t.end_fill()
  #Bell Clapper
  t.up()
  t.setpos(xValue+25,yValue-75)
  t.color(bellColor)
  t.seth(0)
  t.down()
  t.begin_fill()
  t.circle(10)
  t.end_fill()
  #Bell
  t.up()
  t.setpos(xValue,yValue-25)
  t.color(bellColor)
  t.seth(90)
  t.down()
  t.begin_fill()
  t.circle(-25,180)
  t.setpos(xValue+55,yValue-65)
  t.setpos(xValue-5,yValue-65)
  t.end_fill()
def drawBody():
  t.up()
  t.begin_fill()
  t.setpos(xValue,yValue)
  t.seth(-45)
  t.color(outline)
  t.fillcolor(cowColor)
  t.down()
  for x in range(0,2):
    t.circle(330,90)
    t.circle(105,90)
  t.end_fill()
  t.up()
def drawBodySpots():
  #1
  t.up()
  t.setpos(xValue+250,yValue+245)
  t.color(spotColor)
  t.seth(-100)
  t.down()
  t.begin_fill()
  t.circle(35,80)
  t.circle(-40,60)
  t.circle(100,100)
  t.circle(-35,40)
  t.circle(70,34)
  t.seth(105)
  t.circle(105,22)
  t.left(4)
  t.circle(330,40)
  t.end_fill()
  #2
  t.up()
  t.setpos(xValue+150,yValue+235)
  t.seth(-80)
  t.down()
  t.begin_fill()
  t.circle(-50,80)
  t.circle(90,70)
  t.circle(-70,95)
  t.seth(117)
  t.circle(-105,70)
  t.circle(-330,20)
  t.end_fill()
  #3
  t.up()
  t.setpos(xValue+120,yValue-75)
  t.seth(80)
  t.down()
  t.begin_fill()
  t.circle(-45,100)
  t.circle(90,60)
  t.circle(-55,75)
  t.circle(40,30)
  t.circle(-70,42)
  t.seth(-150)
  t.circle(-330,40)
  t.end_fill()
  #4
  t.up()
  t.setpos(xValue+120,yValue+120)
  t.seth(80)
  t.down()
  t.begin_fill()
  t.circle(-60,120)
  t.circle(50,40)
  t.circle(-55,140)
  t.circle(40,30)
  t.circle(-50,100)
  t.circle(45,45)
  t.circle(-50,140)
  t.circle(25,25)
  t.end_fill()
def drawEyes():
  #Whites
    #Left
  t.seth(0)
  t.up()
  t.setpos(xValue-30,yValue+160)
  t.color("white")
  t.down()
  t.begin_fill()
  t.circle(25)
  t.end_fill()
    #Right
  t.up()
  t.setpos(xValue+70,yValue+160)
  t.color("white")
  t.down()
  t.begin_fill()
  t.circle(25)
  t.end_fill()
  #Irises
    #Left
  t.up()
  t.setpos(xValue-30,yValue+170)
  t.color(eyeColor)
  t.down()
  t.begin_fill()
  t.circle(15)
  t.end_fill()
    #Right
  t.up()
  t.setpos(xValue+70,yValue+170)
  t.color(eyeColor)
  t.down()
  t.begin_fill()
  t.circle(15)
  t.end_fill()
  #Pupils
    #Left
  t.up()
  t.setpos(xValue-30,yValue+175)
  t.color("black")
  t.down()
  t.begin_fill()
  t.circle(10)
  t.end_fill()
    #Right
  t.up()
  t.setpos(xValue+70,yValue+175)
  t.color("black")
  t.down()
  t.begin_fill()
  t.circle(10)
  t.end_fill()
def drawHead():
  #Horns
    #Left
  t.up()
  t.setpos(xValue-50,yValue+230)
  t.width(5)
  t.seth(160)
  t.down()
  t.color(hornColor)
  t.begin_fill()
  t.circle(-85,40)
  t.seth(250)
  t.circle(95,55)
  t.setpos(xValue-50,yValue+230)
  t.end_fill()
    #Right
  t.up()
  t.setpos(xValue+90,yValue+230)
  t.seth(20)
  t.down()
  t.color(hornColor)
  t.begin_fill()
  t.circle(85,40)
  t.seth(290)
  t.circle(-95,55)
  t.setpos(xValue+90,yValue+230)
  t.end_fill()
  #Head
  t.up()
  t.seth(0)
  t.width(1)
  t.setpos(xValue+20,yValue+45)
  t.color(outline)
  t.fillcolor(cowColor)
  t.down()
  t.begin_fill()
  t.circle(110)
  t.end_fill()
def drawHeadSpot():
  t.up()
  t.setpos(xValue+30,yValue+265)
  t.color(spotColor)
  t.seth(-10)
  t.down()
  t.begin_fill()
  t.circle(-35,95)
  t.circle(20,50)
  t.circle(-30,100)
  t.circle(35,60)
  t.circle(-40,90)
  t.circle(20,50)
  t.circle(-30,90)
  t.seth(125)
  t.circle(-110,125)
  t.end_fill()
def drawLeg(legX,legY):
  #Leg
  t.up()
  t.begin_fill()
  t.color(outline)
  t.setpos(legX,legY)
  t.seth(-90)
  t.down()
  t.forward(175)
  t.left(90)
  t.forward(75)
  t.left(90)
  t.forward(175)
  t.color(cowColor)
  t.left(90)
  t.forward(75)
  t.end_fill()
  t.up()
  #Hoof
  t.color(hoofColor)
  t.setpos(legX,legY-175)
  t.seth(0)
  t.down()
  t.begin_fill()
  for x in range(0,2):
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.left(90)
  t.end_fill()
def drawLegSpots1():
  #Leg 1
  t.up()
  t.setpos(xValue+20,yValue-25)
  t.color(spotColor)
  t.seth(0)
  t.down()
  t.begin_fill()
  t.circle(-25,105)
  t.circle(10,50)
  t.circle(-40,115)
  t.end_fill()
  #Leg 3
  t.up()
  t.setpos(xValue+320,yValue-20)
  t.color(spotColor)
  t.seth(0)
  t.down()
  t.begin_fill()
  t.circle(-40,115)
  t.circle(10,50)
  t.circle(-30,130)
  t.end_fill()
def drawLegSpots2():
  #Leg 2
  t.up()
  t.setpos(xValue+135,yValue-25)
  t.color(spotColor)
  t.seth(180)
  t.down()
  t.begin_fill()
  t.circle(25,105)
  t.circle(-10,50)
  t.circle(40,115)
  t.end_fill()
  #Leg 4
  t.up()
  t.setpos(xValue+435,yValue-25)
  t.color(spotColor)
  t.seth(180)
  t.down()
  t.begin_fill()
  t.circle(40,115)
  t.circle(-10,50)
  t.circle(30,130)
  t.end_fill()
def drawMouth():
  #Mouth
  t.up()
  t.seth(-45)
  t.setpos(xValue-50,yValue+50)
  t.down()
  t.color(mouthColor)
  t.begin_fill()
  for x in range(0,2):
    t.circle(100,90)
    t.circle(45,90)
  t.end_fill()
  #Nostrils
    #Left
  t.up()
  t.setpos(xValue-40,yValue+80)
  t.down()
  t.color(nostrilColor)
  t.begin_fill()
  t.circle(10)
  t.end_fill()
    #Right
  t.up()
  t.setpos(xValue+70,yValue+80)
  t.down()
  t.color(nostrilColor)
  t.begin_fill()
  t.circle(10)
  t.end_fill()
def drawTail():
  #Tail
  t.up()
  t.width(1)
  t.setpos(xValue+485,yValue+105)
  t.color(outline)
  t.seth(-55)
  t.down()
  t.begin_fill()
  t.forward(125)
  t.right(90)
  t.forward(25)
  t.right(90)
  t.forward(105)
  t.seth(90)
  t.color(cowColor)
  t.forward(25)
  t.end_fill()
  #Hair
  tailHairX1 = xValue+550
  tailHairY1 = yValue+5
  tailHairX2 = xValue+565
  tailHairY2 = yValue-5
  for x in range(0,5):
    t.up()
    t.color(tailColor)
    t.width(5)
    t.setpos(tailHairX1,tailHairY1)
    t.down()
    t.setpos(tailHairX2,tailHairY2)
    tailHairX1 = tailHairX1-3.5
    tailHairY1 = tailHairY1-3
    tailHairX2 = tailHairX2-5.5
    tailHairY2 = tailHairY2-5
  t.width(1)
def drawTailSpot():
  #1
  t.up()
  t.setpos(xValue+491,yValue+95)
  t.color(spotColor)
  t.seth(-127)
  t.down()
  t.begin_fill()
  t.circle(10,90)
  t.circle(-15,45)
  t.circle(15,90)
  t.end_fill()
  #2
  t.up()
  t.setpos(xValue+500,yValue+43)
  t.color(spotColor)
  t.seth(-14)
  t.down()
  t.begin_fill()
  t.circle(-15,60)
  t.circle(10,40)
  t.circle(-15,70)
  t.end_fill()
t.ht()
t.speed(10)

xValue = -200
yValue = -30

bellColor = "gold1"
cowColor = "oldLace"
eyeColor = "deepSkyBlue2"
hoofColor = "gray50"
hornColor = "gray20"
leatherColor = "red3"
mouthColor = "rosyBrown1"
nostrilColor = "gray25"
outline = "peachPuff"
spotColor = "gray30"
tailColor = "gray30"

# #Leg 1
# drawLeg(xValue+20,yValue-5)
# # Leg 3
# drawLeg(xValue+320,yValue-5)
# drawLegSpots1()
drawBody()
# drawTail()
# drawBodySpots()
# drawTailSpot()
# #Leg 2
# drawLeg(xValue+60,yValue-20)
# #Leg 4
# drawLeg(xValue+360,yValue-20)
# drawLegSpots2()
# drawBell()
# drawHead()
# drawHeadSpot()
# drawMouth()
# drawEyes()