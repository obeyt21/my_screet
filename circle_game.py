import turtle
import  time
import random

ekran =turtle.Screen()
ekran.bgcolor("white")
ekran.title("daireyi yakala, skoru tamamla")

score = 0
skore = turtle.Turtle()
skore.penup()
skore.hideturtle()
skore.goto(0, 270)
skore.write(f"Skor: {score}", align="center", font=("Arial", 16, "bold"))

sonuc = turtle.Turtle()
sonuc.penup()
sonuc.hideturtle()
sonuc.goto(0, 250)

daire= turtle.Turtle()
daire.shape("circle")
daire.color("black")
daire.penup()

width = 600
height = 600
ekran.setup(width=width, height=height)

def hareket_et():
    if score ==10:
        return
    x = random.randint(-width//2 +10, width//2 -10)
    y = random.randint(-height//2 +50, height//2 -50)
    daire.goto(x, y)
    ekran.ontimer(hareket_et, 500)

def skor_artir():
    global score
    score +=1
    skore.clear()
    skore.write(f"Skor: {score}", align="center", font=("Arial", 16, "bold"))

    if score ==10:
        sonuc.clear()
        sonuc.write("Tebrikler, skora ulaştınız!", align="center", font=("Arial", 24, "bold"))
        daire.onclick(None)

def daire_tikla(x, y):
    skor_artir()

daire.onclick(daire_tikla)
hareket_et()
ekran.mainloop()
