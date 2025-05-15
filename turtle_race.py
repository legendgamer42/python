import turtle
import time
import random

WIDTH,HEIGHT = 500,500

COLORS = [
    'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink',
    'black', 'gray', 'brown', 'cyan', 'magenta',
]


# class turtle_racer:
#     def __init__(self,speed,color):
#         self.turtle = turtle.Turtle()
#         self.turtle.speed(speed) 
#         self.turtle.color(color)
#         self.turtle.shape('turtle')
        # self.turtle.penup()

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("How many turtles would you like to race (2-10)? ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Must be a Number!")
            continue    
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")

def race(colors):
    turtles = create_turtles(colors)
    time.sleep(5)

    y_positions = [-HEIGHT//2 + 20 for i in range(len(colors))]
    while True:
        for i,racer in enumerate(turtles):
            distance = random.randrange(1,10)
            racer.forward(distance)

            x,y = racer.pos()
            y_positions[i] = y
            
        if max(y_positions) >= HEIGHT // 2 - 10:
            return colors[y_positions.index(max(y_positions))]
            
def create_turtles(colors):
    turtles = []
    y = -HEIGHT//2 + 20 
    spacing = WIDTH// (len(colors) + 1)
    for i, color in enumerate(colors):
        x = -WIDTH//2 + spacing * (i+1)
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.setheading(90)
        racer.penup()
        racer.setpos(x,y)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!')
    screen.update()  # Force an update
    time.sleep(0.1)  # Let the screen appear
def force_focus():
    root = turtle.getcanvas().winfo_toplevel()
    root.lift()
    root.attributes('-topmost', 1)
    root.attributes('-topmost', 0)
racers = get_number_of_racers()

random.shuffle(COLORS)
colors = COLORS[:racers]
init_turtle()
force_focus()


# for i in range(racers):
#     color = colors[i]
#     speed = random.randint(1,10)
#     turtles.append(turtle_racer(speed,color)) 
winner = race(colors)
print(f"the winner is turtle with color: {winner}")
# position_turtles(turtles)
turtle.done()

