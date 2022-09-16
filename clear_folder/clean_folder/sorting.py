from dbm import error
from genericpath import exists
from importlib.resources import path
import os
import sys
import re

from pathlib import Path
from random import randint


import shutil
import gzip
import zipfile

from clean_folder.addition import *

for i in range(2000):
    print(i)
print("|", "_"*50)


def helloworld():
    print("hello world")

# ---------------   NORMALIZE --------------------


def normalize(filepath):
    print("|{:_^50}".format("Normilize"))

    result = ""

    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    if ext == ".gz":
        name, twho_ext = os.path.splitext(name)
        print("| DDa VOT TOT ")
        print(f"| {name} - {twho_ext}")

    print("| - $$$$", filename)

    some = re.findall(r'[a-zA-Z0-9_]', name)
    print("| ", some)
    print(f"|\n| Old name is {os.path.basename(filepath)}")
    for i in name:
        if i in translate:
            result += translate[i]
        elif i not in some:
            i = "_"
            result += i
        else:
            result += i

    if ext == ".gz":
        result += twho_ext
    result += ext

    namedir = os.path.dirname(filepath)
    new_filepath = os.path.join(namedir, result)
    if str(filepath) == str(new_filepath):
        print("| No need changes")
        print("|{}".format("-"*50))

        return new_filepath
    else:
        print("| New name is", os.path.basename(new_filepath))
        os.rename(filepath,  result)
        return new_filepath


# ---------------   MOVE TO  FOLDER --------------------

def move_to_folder(filepat):
    print("|\n|{:_^50}\n|".format("Move to folder"))
    # Удаление .DS_Store
    if os.path.basename(filepat).startswith(".DS"):
        print(
            f"| ------- {os.path.basename(filepat)} ------- DELETE  КУСОК ГОВНА")
        os.remove(filepat)
        return True

    # Тут вызов функции для замены  имени файла

    filepath = normalize(filepat)

    print(f"|---\n| FILEPATH IS - {filepath}")

    name, exp = os.path.splitext(filepath)

    for key_name in extensions:

        need = os.path.join(DIRECTORY, key_name)

        # print(f"|\n| Ключ - {key_name}")
        # print(f"|\n| Значения - {extensions[key_name]}")
        if exp[1::] in extensions[key_name]:
            # --------------- Архивные файлы ----------------

            if exp[1::] in extensions["archives"]:
                print("| Как обычно мой друг)")
                if os.path.isdir(need):
                    print(f"| Существует {key_name}")
                else:
                    print("| Создаем папочку для архивов")
                    print(key_name)

                    os.mkdir(need)
                print("| тут")

                print("| Ииииии")

                try:
                    print("| Попытка")
                    # os.chdir(DIRECTORY)
                    print(os.getcwd(), "get cwd")
                    print("| Filepath is :\n", filepath)
                    print("| Need is :\n", need)
                    os.chdir(need)
                    shutil.unpack_archive(
                        filepath, os.path.basename(name))
                    print("| УСПЕШНО")
                    os.remove(filepath)
                    os.chdir(os.path.dirname(filepath))
                    return True

                except shutil.ReadError as error:
                    print("| --------")
                    print("| Error is - [", error)

                    return "| --------- ola amigo ---------"

            # ---------------- Все кроме архивов ------------------
            else:
                if os.path.isdir(need):
                    print(f"| Существует {key_name}")
                else:
                    print(f"| Создание папки {key_name}")
                    os.mkdir(need)
                try:
                    shutil.move(filepath, need)
                    print(
                        f"| Файл {os.path.basename(filepath)} перемещена в {key_name}")
                    return True
                except shutil.Error:
                    print("PLS WORK")
                except:
                    os.chdir(DIRECTORY)
                    print(
                        f"|\n| Не можем переместить файл {os.path.basename(filepath)} в {key_name}")
                    # проверка на ссуществует ли данный файл в необходимой папке
                    justname = os.path.basename(filepath)
                    print(f"| Just name = {justname}")
                    new_name, exp = os.path.splitext(justname)
                    a = 0
                    while True:
                        run_num = str(randint(0, 999))
                        ultras = new_name+run_num+exp
                        print(f"|\n| ULTRAS - {ultras}")
                        a += 1
                        if a == 50:
                            print("50 mtf")
                            break
                        elif ultras in need:
                            print("| Даже такое имя уже есть")
                            print("| Еще раз")
                            continue
                        else:

                            print('| Да вот тут сидим, чилим')
                            print("|---\n|", ultras, "\n| ULTRAS")
                            print("|---\n|", need, "\n| NEED")
                            print("|---\n| -", filepath, "\n| FILEPATH")
                            os.rename(filepath, ultras)
                            print("daAAA")

                            shutil.move(ultras, need)
                            print(
                                f"| Файл -  {ultras} перемещен в {key_name} ")
                            return True


# ---------------   SORTING DIRECTORIES --------------------


def sorting_directories(path_to_file):

    if os.path.basename(path_to_file).startswith(".DS_"):
        print(
            f"| ------- {os.path.basename(path_to_file)} ------- КУСОК ГОВНА УДАЛЕН")
        os.remove(path_to_file)
        return True
        # test
        # sorting_directories(os.path.dirname(path_to_file))

    os.chdir(path_to_file)
    dir = Path(path_to_file)
    print(f"|\n| Сортировка папки - {os.path.basename(path_to_file)}")
    here_need_a_sort = True
    if len(os.listdir(path_to_file)) == 0:
        print("| tut PUSTO")
        os.rmdir(path_to_file)
        sorting_directories(os.path.dirname(path_to_file))
        here_need_a_sort = False
    new_dir = Path(DIRECTORY)

    while here_need_a_sort:
        for filepath in dir.iterdir():
            if os.path.exists(filepath):
                pass
            else:
                continue
            justname = os.path.basename(filepath)
            print(f"|\n| Файл - {justname} --- =+")
            if os.path.isdir(filepath):
                print(
                    f"|\n| Этот файл директория - {justname}")
                if justname in extensions:
                    print(f"| Эта папка не для сортировки - {justname}")
                    continue
                else:
                    if len(os.listdir(filepath)) == 0:
                        print("| В этой папке 0 файлов")
                        print("| Идет удаление")
                        os.rmdir(filepath)
                        print("~"*50)
                        continue
                    else:
                        print("|"+chr(684)*50)
                        sorting_directories(filepath)
            else:
                if os.path.basename(filepath).startswith(".DS_"):
                    print("попытка   уталить каку")
                    try:
                        os.remove(filepath)
                        continue           # ------------- tut
                    except FileNotFoundError:
                        here_need_a_sort = False
                else:
                    # breakpoint()
                    print("| Выполняем Move to folder")
                    move_to_folder(filepath)
                    continue  # ----------- tut

            print("|{:=^50}".format("-Konets-"))
        here_need_a_sort = False

        print("{:_^50}".format("ФИНИШНАЯ ПРЯМАЯ"))
        try:
            for noneeddir in new_dir.iterdir():
                if os.path.basename(noneeddir) in extensions:
                    print(
                        f"| Файл {os.path.basename(noneeddir)} не для проверки")
                    continue
                elif os.path.basename(noneeddir).startswith(".DS"):
                    print("Только тут  я рад видеть дс стор)")
                    here_need_a_sort = False
                    return "Ok"
                    break
                elif os.path.basename(noneeddir) not in extensions:
                    print(f"| NONEDIR is - {os.path.basename(noneeddir)}\n|")
                    print("{:.^50}".format("Вход в рекурсию на конце"))
                    try:
                        sorting_directories(noneeddir)
                    except:
                        print('its ok')
                        break
                else:
                    print("ELSE")
                    return "FINE"
                    break
        except:
            print("its ok ")

    return "| WORK IS DONE\n|{:_^50}".format("Thanks for using")


DIRECTORY = ""


def main():
    DIR = sys.argv[1]
    DIRECTORY = DIR
    sorting_directories(DIRECTORY)
    print("Yep i hope this work)\nThanks for using :)")
