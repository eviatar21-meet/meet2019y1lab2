import turtle

def add_new(event):
    """makes a new turtle, calculates the turtle coordinates based on the mouse position,
    then sends the turtle there"""
    t = turtle.Turtle()
    screen_w, screen_h = t.screen._window_size()
    t.goto(event.x - screen_w//2, screen_h //2 - event.y)

t = turtle.Turtle()
t.pendown()
t.hideturtle()
t.screen.cv.master.bind('<space>', add_new)
#turtle.exitonclick()
