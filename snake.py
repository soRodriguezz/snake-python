#Librerias python
import turtle
import time
import random

# para decrecer la velocidad de la cabeza
postpone = 0.1

# Marcador
score = 0
high_score = 0

# Variable para salir del juego
salir = True

# Configuracion de la ventana
window = turtle.Screen()
window.title("Snake")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Crear comida
eat = turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("red")
eat.penup()
eat.goto(0,100)

# Cuerpo serpiente
segment = []

# texto marcador
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

# texto para salir
text_exit = turtle.Turtle()
text_exit.speed(0)
text_exit.color("white")
text_exit.penup()
text_exit.hideturtle()
text_exit.goto(0,-260)
text_exit.write("Press x to exit", align="center", font=("Courier", 10, "normal"))

# Funciones de movimiento
def _up():
    head.direction = "up"

def _down():
    head.direction = "down"

def _left():
    head.direction = "left"

def _right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def press_exit():
    window.bye()

# Teclado
window.listen()
window.onkeypress(_up, "Up")
window.onkeypress(_down, "Down")
window.onkeypress(_left, "Left")
window.onkeypress(_right, "Right")
window.onkeypress(press_exit, "x")

while salir:
    window.update()

    # Colisiones bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Esconder segmentos
        for segment in segment:
            segment.goto(1000,1000)

        # limpiar lista de segmentos
        segment = []

        # reiniciar marcador
        score = 0
        text.clear()
        text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
    # Colisiones comida
    if head.distance(eat) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-240, 240)
        eat.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        # Aumentar marcador
        score += 1
        if score > high_score:
            high_score = score
        
        text.clear()
        text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        

    # colisiones cuerpo
    for segmen in segment:
        if segmen.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
     # Esconder segmentos
            for segmen in segment:
                segmen.goto(1000,1000)

            # limpiar lista de segmentos
            segment = []

            # limpiar campos
            score = 0
            text.clear()
            text.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    # Mover cuerpo serpiente
    totalSeg = len(segment)
    for index in range(totalSeg-1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x,y)
    
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()
    time.sleep(postpone)
