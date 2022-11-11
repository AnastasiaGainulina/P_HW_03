# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player = (int(input('Введите кол-во игроков 1 или 2: ')))
if player ==2:
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = int(input("Введите количество конфет на столе: "))
    step = randint(0,2)
    if step:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0 
    counter2 = 0

    while value > 28:
        if step:
            k = input_dat(player1)
            counter1 += k
            value -= k
            step = False
            p_print(player1, k, counter1, value)
        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            step = True
            p_print(player2, k, counter2, value)

    if step:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")
elif player==1:
    player1 = input("Введите имя первого игрока: ")
    player2 = "Bot"
    value = int(input("Введите количество конфет на столе: "))
    step = randint(0,2)
    if step:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0 
    counter2 = 0

    while value > 28:
        if step:
            k = input_dat(player1)
            counter1 += k
            value -= k
            step = False
            p_print(player1, k, counter1, value)
        else:
            k = randint(1,29)
            counter2 += k
            value -= k
            step = True
            p_print(player2, k, counter2, value)

    if step:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")
else:
    print('Введите 1 или 2')
