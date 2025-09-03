#>>---WELCOME!! DONE BY:VISHNU_ANIL_MEC EV(25-29)---<<
import turtle
turtle.tracer(0) #---for instant results
cursor = turtle.Turtle()
cursor.pensize(5) #---size of pen
cursor.shape("classic")#---arrow shape
cursor.speed(10)#---if its drawing, the cursor speed


def colorPicker(): #---Function for choosing colors for the beautiful curved outer circle pattern
    allcolors = [
     # Yellows
    "Yellow", "Gold",

    # Oranges
    "Orange", "DarkOrange",

    # Reds
    "Red", "Firebrick",]
    while True:
        yield from allcolors 

#SCREEN SIZE
screen = turtle.Screen()
screen.setup(width=1500, height=1000)


#FIRST OUTER CIRCLE
cursor.color("yellow green","Dark orchid")
cursor.pensize(15)
cursor.penup()
cursor.goto(-29.99999999999988,79.99999999999974) #---for alignment
cursor.forward(325)
cursor.right(93)
cursor.pendown()
cursor.begin_fill() 
cursor.circle(-323)
cursor.end_fill() 
cursor.pensize(5)


#MULTIPLE CURVES PATTERN -->

#Alignment of curser
#-----------------------
cursor.penup()
cursor.home()
cursor.pendown()
colour = colorPicker()
cursor.penup()
cursor.left(90)
cursor.forward(80)
cursor.left(90)
cursor.forward(30)
cursor.left(90)
cursor.pendown()
x=cursor.xcor() #---getting x and y coordinates for new centre determination
y=cursor.ycor()
cursor.goto(x,y)
#-----------------------

#Formation of pattern
#-----------------------
for i in range(37):
    if i!=36:
        cursor.color(next(colour),next(colour)) #---shifting colors using yield function(prevents complex loops and more efficient )
        cursor.begin_fill()
        cursor.circle(150,180)#---first curve
        cursor.penup()
        cursor.right(20)
        cursor.circle(162,-140)#---second reverse curve perfectly allligned
        cursor.end_fill()
        cursor.home()
        cursor.goto(x,y+20)
        cursor.left(i*10)#---restart with new direction(which is multiple of 10)
        cursor.pendown()
    else:#---final curve allignment since center not needed
        cursor.color(next(colour),next(colour)) 
        cursor.begin_fill()
        cursor.circle(150,180)
        cursor.penup()
        cursor.right(20)
        cursor.circle(200,-140)
        cursor.end_fill()
        cursor.home()
        cursor.goto(x,y+20)
        cursor.left(i*10)
        cursor.pendown()
      

cursor.penup()
cursor.home()
#-----------------------

#FIRST OUTER BIG FLOWER-->  

#Allignment of curser
#-----------------------
cursor.home()
cursor.goto(x,y)
cursor.right(175)
cursor.forward(115)
cursor.left(90)
cursor.forward(80)
cursor.left(46)
cursor.forward(125)
cursor.pendown()
#-----------------------

#Formation of pattern
#-----------------------
for i in range(9):
    cursor.pensize(6)
    cursor.color("magenta4","dark orchid")
    cursor.begin_fill()
    cursor.circle(260,20)
    cursor.left(70)
    cursor.circle(260,20)
    cursor.right(70)
    cursor.end_fill()
#-----------------------

#SECOND OUTER BIG FLOWER-->

#Allignment of curser
#-----------------------
cursor.penup()
cursor.home()
cursor.goto(x,y)
cursor.right(150)
cursor.forward(120)
cursor.left(90)
cursor.forward(70)
cursor.left(46)
cursor.forward(125)
cursor.pendown()
#-----------------------

#Formation of pattern
#-----------------------
for i in range(9):
    cursor.pensize(6)
    cursor.color("DeepPink4","deep pink")
    cursor.begin_fill()
    cursor.circle(230,20)
    cursor.left(60)
    cursor.circle(230,20)
    cursor.right(60)
    cursor.end_fill()
#-----------------------

#INNER BIG CIRCLE-->
#Allignment of curser
#-----------------------
cursor.penup()
cursor.color("gold1","olive")
cursor.home()
cursor.goto(x,y)
cursor.forward(120)
cursor.left(180)
cursor.forward(280)
cursor.left(98)
cursor.pensize(30)
#-----------------------

#Formation of pattern
#-----------------------
cursor.pendown()
cursor.begin_fill()
cursor.circle(165)
cursor.end_fill()
cursor.penup()
cursor.home()
#-----------------------

#INNER FLOWER-->

#Allignment of curser
#-----------------------   
cursor.right(180)
cursor.forward(47)
cursor.right(180)
cursor.pendown()
cursor.pensize(5)
#-----------------------

#Formation of pattern
#-----------------------
for i in range(9): 
    cursor.color("orange1","red")
    cursor.begin_fill()       
    cursor.circle(200, 60)
    cursor.pensize(3)


    cursor.penup()#---Adding tiny circles along the same loop
    cursor.forward(26)
    cursor.right(180)
    cursor.pendown()
    cursor.circle(12)
    cursor.penup()
    cursor.left(180)
    cursor.right(180)
    cursor.forward(26)
    cursor.left(180)
    cursor.pensize(5)#---finishing 1 tiny circle at each loop

    cursor.pendown() #---continuing inner flower        
    cursor.left(60)             
    cursor.circle(200, 60)       
    cursor.left(20)    
    cursor.end_fill()
  
for i in range(8):   #---Finishing incomplete outlines
    cursor.color("orange1")
    cursor.circle(200, 60)       
    cursor.left(60)             
    cursor.circle(200, 60)       
    cursor.left(20)
    if i==7:
        cursor.penup()
        break 
#-----------------------

#INNER HEXAGONAL FLOWER-->
#Allignment of curser
#-----------------------   
cursor.penup()
cursor.home()
cursor.left(90)
cursor.forward(160)
cursor.right(90)
cursor.forward(10)
cursor.left(180)
cursor.forward(60)
cursor.right(90)
cursor.forward(10)
cursor.left(90)

cursor.color("orange1","gold1")
cursor.pendown()
#-----------------------

#Formation of pattern
#-----------------------
for i in range(6):
    cursor.begin_fill()  
    cursor.circle(80, 30)       
    cursor.left(30)  
    cursor.circle(80, 30) 
    cursor.right(30)
    cursor.end_fill()
#-----------------------
    
#FINAL INNER MOST CIRCLE-->

#Allignment of curser
#-----------------------   
cursor.penup()
cursor.home()
cursor.left(90.5)
cursor.forward(160)
cursor.left(90)
cursor.forward(30)
#-----------------------

#Formation of pattern
#-----------------------
cursor.pendown()
cursor.color("orange","navajo white1") 
cursor.begin_fill() 
cursor.circle(60)
cursor.end_fill()
#-----------------------

#FINAL INNERMOST TINY FLOWER-->

#Allignment of curser
#-----------------------
cursor.penup()
cursor.left(90)
cursor.forward(60)
cursor.pendown()
cursor.pensize(3)

cursor.color("violetred","hotpink")
#-----------------------

#Formation of pattern
#-----------------------
for i in range(13): 
    cursor.begin_fill()        
    cursor.circle(50, 60)       
    cursor.left(120)            
    cursor.circle(50, 60)       
    cursor.left(10)   
    cursor.end_fill()
#-----------------------
cursor.hideturtle()#---hide the cursor
turtle.update()#---for instant results!
turtle.done()#---GG

#--------------------THANK YOU!#--------------------
