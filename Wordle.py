import turtle
import random

image = "winning_image.gif"
image2 = "game-over.gif"
gif = turtle.Turtle()
game_over = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(700, 500)
words_list = ["abuse", "throw", "south", "other", "crowd", "dream", "likes", "taste", "avoid", "where", "brave", "after", "earth"]
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
screen.listen()
shapes = []
comp_choice = (random.choice(words_list)).lower()
screen.addshape(image)
screen.addshape(image2)
gif.shape(image)
game_over.shape(image2)
gif.hideturtle()
game_over.hideturtle()

print(comp_choice)

def draw_square(length):
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    shapes.append(((turtle.xcor()+20), turtle.ycor()-40))

def draw_boxes():
    for i in range(5):
        turtle.pendown()
        draw_square(40)
        turtle.penup()
        turtle.fd(60)


def character_dashes():
    turtle.clear()
    y = 200
    turtle.setposition(-130, y)
    for i in range(6):
        draw_boxes()
        y -= 50
        turtle.setposition(-130, y)
    game = True
    length = 0
    attempts = 1
    while game:
        if attempts > 6:
            turtle.clear()
            turtle.goto(-20, -250)
            turtle.pendown()
            turtle.write("You Ran Out Of Attempts", align="center", font=("Comic Sans MS", 30, "normal"))
            turtle.penup()
            game_over.showturtle()
            turtle.bye()
        user_ans = ""
        for letter in comp_choice:
            user_guess = (screen.textinput(title=f"Guess The word", prompt="ENTER A LETTER?")).lower()
            turtle.goto(shapes[length])
            turtle.pendown()
            if user_guess in comp_choice:
                turtle.color("orange")
                if letter == user_guess:
                    turtle.color("green")
            user_ans += user_guess
            turtle.write(user_guess, align="center", font=("Comic Sans MS", 20, "normal"))
            length += 1
            turtle.color("black")
            turtle.penup()
        attempts += 1
        if user_ans == comp_choice:
            turtle.clear()
            turtle.goto(-20, -300)
            turtle.pendown()
            turtle.color("black")
            turtle.write("YOU GOT IT RIGHT", align="center", font=("Comic Sans MS", 30, "normal"))
            turtle.penup()
            gif.showturtle()
            game = False




print(shapes)

def display():
    screen.listen()
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.write("RULES", align="left", font=("Comic Sans MS", 30, "normal"))
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.write("EXIT", align="left", font=("Comic Sans MS", 30, "normal"))
    turtle.penup()
    turtle.goto(250, 0)
    turtle.pendown()
    turtle.write("PLAY", align="left", font=("Comic Sans MS", 30, "normal"))
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.write("SPACE", align="left", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.write("ESCAPE", align="left", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    turtle.goto(250, -50)
    turtle.pendown()
    turtle.write("ENTER", align="left", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    screen.onkey(key="space", fun=rules)
    screen.onkey(key="Escape", fun=screen.bye)
    screen.onkey(key="Return", fun=character_dashes)


def rules():
    turtle.clear()
    turtle.goto(-30, 200)
    turtle.pendown()
    turtle.write("Rule 1 : YOU CAN ONLY CHOOSE 5 LETTER WORDS", align="center", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    turtle.goto(-30, 150)
    turtle.pendown()
    turtle.write("Rule 2: IF ONE OF THE LETTER IS IN THE WORD BUT NOT THE RIGHT PLACE IT WOULD BE HIGHLIGHTED IN ORANGE", align="center", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    turtle.goto(-30, 100)
    turtle.pendown()
    turtle.write("Rule 3 : IF ONE OF THE LETTER IS IN THE WORD AND AT THE RIGHT PLACE IT WILL BE HIGHLIGHTED IN GREEN", align="center", font=("Comic Sans MS", 10 ,"normal"))
    turtle.penup()
    turtle.goto(-30, 50)
    turtle.pendown()
    turtle.write("Rule 4 : IF THE LETTER IS NOT IN THE WORD IT WILL BE HIGHLIGHTED IN GREY.", align="center", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.write("ENTER", align="center", font=("Comic Sans MS", 10, "normal"))
    turtle.penup()
    screen.onkey(key="Return", fun=character_dashes)

display()
screen.exitonclick()