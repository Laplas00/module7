
from operator import length_hint
import random

length_snake = 2

hea = chr(169)
print(hea)
block = [[["1 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["2 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["3 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["4 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["5 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["6 "], ["."], ["-"], ["O"], ["-"], ["."], ["."], ["."], ["."], ["."]],
         [["7 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["8 "], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["9 "], ["."], ["."], ["."], [hea], ["."], ["."], ["."], ["."], ["."]],
         [["10"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["11"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["12"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["13"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["14"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["15"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]],
         [["16"], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."], ["."]]]


def controll(spisok, direction):
    # программа считает тут строки
    # И в заависимости от строки на которой  я нахожусь
    # она делает расчеты по движению
    line = 0
    for i in spisok:

        try:
            here = i.index(["O"])

            match direction:
                case "d":
                    i.pop(here+1)
                    i.insert(here, ['.'])
                    return spisok
                case "a":

                    print(i, "\n")
                    i.pop(here-1)
                    i.insert(here, ['.'])

                    return spisok
                case "w":

                    i.pop(here)
                    i.insert(here, ["."])
                    spisok[line-1].pop(here)
                    spisok[line-1].insert(here, ["O"])
                    return spisok
                case "s":
                    print(spisok[line])
                    i.pop(here)
                    i.insert(here, ["."])
                    spisok[line+1].pop(here)
                    spisok = spisok[line+1].insert(here, ["O"])
                    print(line+1, "line")

                    return spisok
                case "r":
                    spisok = block
                    return spisok

        finally:
            line += 1

            continue


def random_eat(list):
    # создает "еду" в списке из списков
    # который дается
    # возвращает "+" в одной из ячеек (раандомно)
    yep = 0
    for i in list:
        if [hea] in i:
            yep = 1
            break
        else:
            continue
    if yep == 0:
        inline = random.randint(1, len(list[0]))
        line = random.randint(0, len(list))
        try:
            list[line][inline] = [hea]
        except IndexError:
            pass
        return list
    else:

        return list


def snake(list):
    pass


process = True
while process:
    score = 0
    random_eat(block)
    for i in range(len(block)):
        print(block[i], "---")
    move = input()
    match move:
        case "p":
            process = False
            break
        case "d": controll(block, move)
        case "a": controll(block, move)
        case "w": controll(block, move)
        case "s": controll(block, move)

    #     for di in i:
    #         if di == "O":
    #             move = input('')
    #             if move == "d":
    #                 di.
