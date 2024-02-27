# Импортируем модуль turtle, который позволяет рисовать графику
import turtle
import random
# Создаем черепаху, которая будет рисовать
t = turtle.Turtle()

# Устанавливаем скорость рисования
t.speed(0)

# Создаем список цветов, которые будем использовать
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Создаем переменную, которая будет хранить толщину линии
thickness = 5

# Создаем цикл, который будет повторяться 36 раз
for i in range(36):

    # Выбираем случайный цвет из списка
    t.color(random.choice(colors))

    # Устанавливаем толщину линии
    t.pensize(thickness)

    # Рисуем квадрат
    for j in range(4):
        t.forward(100)
        t.right(90)

    # Поворачиваем черепаху на 10 градусов
    t.right(10)

    # Уменьшаем толщину линии на 0.1
    thickness -= 0.1

# Добавляем код, который позволяет управлять черепахой с клавиатуры
# Создаем функции, которые определяют движение черепахи
def go_up():
    t.setheading(90) # Устанавливаем направление черепахи вверх
    t.forward(10) # Двигаем черепаху вперед на 10 пикселей

def go_down():
    t.setheading(270) # Устанавливаем направление черепахи вниз
    t.forward(10) # Двигаем черепаху вперед на 10 пикселей

def go_left():
    t.setheading(180) # Устанавливаем направление черепахи влево
    t.forward(10) # Двигаем черепаху вперед на 10 пикселей

def go_right():
    t.setheading(0) # Устанавливаем направление черепахи вправо
    t.forward(10) # Двигаем черепаху вперед на 10 пикселей

# Добавляем код, который позволяет менять цвет и толщину черепахи с клавиатуры
# Создаем функции, которые определяют смену цвета и толщины
def change_color():
    t.color(random.choice(colors)) # Выбираем случайный цвет из списка

def increase_thickness():
    global thickness # Объявляем толщину как глобальную переменную
    thickness += 1 # Увеличиваем толщину на 1
    t.pensize(thickness) # Устанавливаем новую толщину линии

def decrease_thickness():
    global thickness # Объявляем толщину как глобальную переменную
    thickness -= 1 # Уменьшаем толщину на 1
    t.pensize(thickness) # Устанавливаем новую толщину линии

# Связываем функции с клавишами
turtle.onkey(go_up, "Up") # При нажатии на клавишу "Вверх" вызываем функцию go_up
turtle.onkey(go_down, "Down") # При нажатии на клавишу "Вниз" вызываем функцию go_down
turtle.onkey(go_left, "Left") # При нажатии на клавишу "Влево" вызываем функцию go_left
turtle.onkey(go_right, "Right") # При нажатии на клавишу "Вправо" вызываем функцию go_right
turtle.onkey(change_color, "c") # При нажатии на клавишу "c" вызываем функцию change_color
turtle.onkey(increase_thickness, "+") # При нажатии на клавишу "+" вызываем функцию increase_thickness
turtle.onkey(decrease_thickness, "-") # При нажатии на клавишу "-" вызываем функцию decrease_thickness

# Включаем режим ожидания нажатия клавиш
turtle.listen()

# Завершаем рисование
turtle.done()