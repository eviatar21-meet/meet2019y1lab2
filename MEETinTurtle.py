import turtle 

turtle.penup() 
turtle.goto(-200,-100) 
turtle.pendown()

#M
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

turtle.penup()
#E
turtle.goto(-200+150, -100)
turtle.pendown()
turtle.goto(-50,100)
turtle.goto(50,100)
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.goto(50,0)
turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(50,-100)

turtle.penup()
#E
turtle.goto(100, -100)
turtle.pendown()
turtle.goto(100,100)
turtle.goto(200,100)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(200,0)
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(200,-100)

turtle.penup()

#T
turtle.goto(300,-100)
turtle.pendown()
turtle.goto(300, 100)
turtle.penup()
turtle.goto(250,100)
turtle.pendown()
turtle.goto(350,100)

turtle.mainloop() 

