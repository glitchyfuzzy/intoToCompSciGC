# Program name: Bouncing Ball
# Program description: Creates a pong game
# Author: Saran Wagner
# Date: February 5 2023

import tkinter as tk

root = tk.Tk()

width = 900
height = 500

# Makes canvas
canvas = tk.Canvas(root, bg='green', width=width, height=height)
canvas.pack()

# Creates ball
ball = canvas.create_oval(430, 10, 470, 50, fill='black')

# Creates paddle
paddleY = height - 20
paddle = canvas.create_rectangle(width//2-50, paddleY, width//2+50, paddleY+10, fill='black')

# Ball moving speed
xSpeed = ySpeed = 3

# Function that moves ball
def moveBall():
    global xSpeed, ySpeed
    x1, y1, x2, y2 = canvas.coords(ball)
    # If wall hits, reverse
    if x1 <= 0 or x2 >= width:
        xSpeed = -xSpeed
    if y1 <=0:
        ySpeed = -ySpeed + 1
    # Calcs center x of ball
    elif y2 >= paddleY:
        cx = (x1 + x2) // 2
        # Checks if plattform is hit
        px1, _, px2, _ = canvas.coords(paddle)
        if px1 <= cx <= px2:
            ySpeed = -ySpeed - 1
        else:
            canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 35), fill='red')
            return
    canvas.move(ball, xSpeed, ySpeed)
    canvas.after(20, moveBall)

# Moves paddle right
def paddleRight(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    # Checks if paddle is moved beyond right wall
    if x2 < width:
        dx = min(width-x2, 18)
        canvas.move(paddle, dx, 0)

# Moves paddle left
def paddleLeft(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    # Checks if paddle is moved beyond left wall
    if x1 > 0:
        dx = min(x1, 18)
        canvas.move(paddle, -dx, 0)

# Calls paddle right/left funtions
canvas.bind_all('<Right>', paddleRight)
canvas.bind_all('<Left>', paddleLeft)

# Calls ball moving function
moveBall()

# Calls main loop
root.mainloop()