import random


# Игра в гоночки
# Заадний фон всегд аходит вниз
# машина управляется прямым нажатием


def city_builder():
    for i in range(50):
        print("|{:<15}|{:.^30}|{:>15}|".format(chr(955),".",chr(955)))


car = "[=]"

wood_line = random.randint(0,15)

print(wood_line)

road_and_city = '{:.<15}{:.^30}{:.>15}'.format(wood_line*"|", car, "|")

# for i in range(40):

#     line = '{:.<15}{:.^30}{:.>15}'.format("|", car, "|")
#     print(line)


print(city_builder())

