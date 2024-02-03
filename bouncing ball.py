from tkinter import *  # Import all definitions from tkinter
from random import randint
# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))  # Add a random digit
    return color
# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0  # Starting center position
        self.y = 0
        self.dx = 2  # Move right by default
        self.dy = 3  # Move down by default
        self.radius = 15  # The radius is fixed
        self.color = getRandomColor()  # Get random color
class BounceBalls:
    def __init__(self):
        self.ballList = []
        window = Tk()  # Create a window
        window.title("Bouncing Balls")  # Set a title
        self.width = 550  # Width of the self.canvas
        self.height = 350  # Height of the self.canvas
        self.canvas = Canvas(window, bg="white",
                             width=self.width, height=self.height)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text="Stop", bg='red', command=self.stop)
        btStop.pack(side=LEFT)
        btResume = Button(frame, text="Resume", bg='yellow', command=self.resume)
        btResume.pack(side=LEFT)
        btAdd = Button(frame, text="+", bg='green', command=self.add)
        btAdd.pack(side=LEFT)
        btRemove = Button(frame, text="-", bg='green', command=self.remove)
        btRemove.pack(side=LEFT)
        btFaster = Button(frame, text="Faster", bg='cyan', command=self.fast)
        btFaster.pack(side=LEFT)
        btSlower = Button(frame, text="Slower", bg='cyan', command=self.slow)
        btSlower.pack(side=LEFT)
        self.sleepTime = 100  # Set a sleep time
        self.isStopped = False
        self.animate()
        self.ballSpeed = 3
        window.mainloop()
    def stop(self):  # Stop animation
        self.isStopped = True
    def resume(self):  # Resume animation
        self.isStopped = False
        self.animate()
    def add(self):  # Add a new ball
        self.ballList.append(Ball())
    def remove(self):  # Remove the last ball
        self.ballList.pop()
    def fast(self):  # Speed-up the ball
        self.ballSpeed = 5
    def slow(self):  # Speed down the ball
        self.ballSpeed = 2
    def animate(self):  # Animate ball movements
        while not self.isStopped:
            self.canvas.after(self.sleepTime)  # Sleep
            self.canvas.update()  # Update self.canvas
            self.canvas.delete("ball")
            for ball in self.ballList:
                self.redisplayBall(ball)
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius,
                                ball.y - ball.radius, ball.x + ball.radius,
                                ball.y + ball.radius, fill=ball.color, tags="ball")
    def ballSpeed(self):
        self.fast()
        self.slow()
BounceBalls()  # Create GUI