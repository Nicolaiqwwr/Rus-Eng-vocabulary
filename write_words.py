# Словарь пдля записи Английских слов
# -*- coding in UTF-8 -*-
# RU - EN vocabulary: bild 0.5
# Рус - Англ словарь: Сборка 0.5


import os
import pickle
import time


# Создание резервной копии словаря
# Проверка на существование файла
check_file = os.path.exists("vocabulary.data")
check_file2 = os.path.exists("copi_vocabu.data")
check_file3 = os.path.exists("text_book.data")
check_file4 = os.path.exists("copi_TextBook.data")
check_file5 = os.path.exists("phrese_vb.data")
check_file6 = os.path.exists("copi_phrVB.data")

# Создание файла для записи в словарь если он отсутствует
if check_file == False:
    with open("vocabulary.data","wb") as f:
        print("Создан фаил для записи")
        time.sleep(1.5)

# Создание файла для записи резервных копий если он отсутствует
if check_file2 == False:
    with open("copi_vocabu.data","wb") as f:
        print("Создан фаил резервного копирования записи")
        time.sleep(1.5)

# Сохдание файла для записи текстов если он отсутствует
if check_file3 == False:
    print("Создан фаил для сохранения текстов")
    with open("text_book.data", 'wb') as f:
        time.sleep(1.5)

# Создание файла для записи копий текстами
if check_file4 == False:
    print("Создан фаил для резервного копирования текстов")
    with open("copi_TextBook.data", "wb") as f:
        time.sleep(1)

# Создание файла для записи фраз
if check_file5 == False:
    print("Создан фаил для записи фраз")
    with open("phrese_vb.data", "wb") as f:
        time.sleep(1)

# Создание файла для резервного копирования фраз
if check_file6 == False:
    print("Создание файла для резервной записи фраз")
    with open("copi_phrVB.data", "wb") as f:
        time.sleep(1)



# Модуль для проверки ввода

instructions = True

def SkanIn(a):

    """ Проверка ввода пользователя """

    listABS = ("""АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz,!?-/*-+.()=@#$%^&:'\"<>№;% """)
    if a == '':
        return True

    # Проверка ввода пользоватея
    for i in listABS:
        for o in a:
            if o == i:
                print("Введено не верное значение!")
                return True


def seyHi():

    """ Приветствие """

    global instructions
    print("""
Инструкция к началу работы.

0 - Выход
1 - Сделать запись в словарь
2 - Чтение
3 - Редактирование
4 - Работа с текстом и переводом
5 - Работа с фразами
6 - Удаление
9 - Повторение инструкий
    """)
    print()
    if instructions == True:
        instructions = False




class Work_vocablary():
    """Работа с данными словаря """

    def __init__(self):
        self.list = {"Рус":"Eng"}
        self.Rus = None
        self.Eng = None
        self.askU = None
        self.askU2 = None
        self.askU3 = None
        self.askU4 = None
        self.Text = " "
        self.Text2 = " "
        self.adress = ("vocabulary.data",
                       'text_book.data',
                       'phrese_vb.data')



    def Write(self):

        # Запись в словарь
        while True:
            print ("0 - выход")
            self.Rus = input("\nРус\n-->")
            if self.Rus == "0":
                break
            self.Eng = input("Eng\n-->")

            # Проверка на существование значения в сохранении
            if os.path.getsize(self.adress[0]) > 0:
                with open(self.adress[0],"rb+") as f:
                    self.list.update(pickle.load(f))
                    for i,s in self.list.items():
                        if self.Rus == i:
                            self.askU4 = True
                            print("Это слово есть в словаре")
                            continue

                        if self.Eng == s:
                            self.askU4 = True
                            print("Это слово есть в словаре")
                            continue

            if self.askU4:
                continue


            self.list[self.Rus] = self.Eng

            if os.path.getsize("vocabulary.data") > 0:
                with open("vocabulary.data", "rb+") as f:
                    self.list.update(pickle.load(f))

                with open("vocabulary.data", "wb") as f:
                    pickle.dump(self.list, f)
                    self.list.clear()


            else:
                with open("vocabulary.data", "wb") as f:
                    pickle.dump(self.list, f)
                self.list.clear()

    def Read(self):

        # Чтение словаря
        while True:
            if os.path.getsize("vocabulary.data") == 0:
                print("\nСловарь пуст\n")
                break

            self.askU = input("\nКоманды для чтения:\n1 - Читать все\n2 - Поиск слова или перевода\n3 - Выход из режима чтения\n-->")
            print("")

            # Проверка ввода пользователя
            self.askU2 = SkanIn(self.askU)
            if self.askU2:
                continue
            else:
                self.askU = int(self.askU)


            if self.askU == 1:
                # Читать все
                with open("vocabulary.data", "rb+") as f:
                    self.list.update(pickle.load(f))
                    for i,s in self.list.items():
                        print(i, " == ",s)
                    print()
                self.list.clear()


            elif self.askU == 2:
                # поиск по ключу
                with open("vocabulary.data", "rb+") as f:
                    self.list.update(pickle.load(f))

                    self.askU2 = input("\nВыбери язык\n1 - Рус\n2 - Eng\n-->")

                    # Проверка ввода пользователя
                    self.askU3 = SkanIn(self.askU2)
                    if self.askU3:
                        continue
                    else:
                        self.askU2 = int(self.askU2)

                    if self.askU2 == 1:

                        # Поиск по ключу
                        self.askU3 = input("\nВведи на Рус\n-->")
                        for a,s in self.list.items():
                            if a == self.askU3:
                                print(a,"-", s,'\n')
                        self.list.clear()

                    elif self.askU2 == 2:

                        # Поиск по значению
                        self.askU3 = input("\nВведи на Eng\n-->")
                        for a,s in self.list.items():
                            if s == self.askU3:
                                print(a,"-", s,'\n')
                        self.list.clear()

            elif self.askU == 3:
                # Выход
                break

            else:
                print("\nТакой команды нет\n")

    def Edit_vc(self):
        # Редактирование

        while True:
            # проверка на существование файла
            if os.path.getsize("vocabulary.data") == 0:
                print("\nСловарь пуст\n")
                break

            self.askU = input("Выберите язык редактирования:\n1 - Рус\n2 - Eng\n3 - Выход\n-->")

            # Проверка ввода пользователя
            self.askU2 = SkanIn(self.askU)
            if self.askU2:
                continue
            else:
                self.askU = int(self.askU)

            # Выполнение коман редактирования
            if self.askU == 1:

                # На руском
                with open("vocabulary.data", 'rb+') as f:
                    self.list.update(pickle.load(f))

                self.askU3 = input("\nВведи редактируемое слово на Рус:\n-->")
                self.askU2 = input("\nВведи исправленный вариант\n--> ")

                # Проверка на существование значения в сохранении
                if os.path.getsize(self.adress[0]) > 0:
                    with open(self.adress[0], "rb+") as f:
                        self.list.update(pickle.load(f))
                        for i in self.list:
                            if self.askU2 == i:
                                self.askU4 = True
                                break

                if self.askU4:
                    print("\nТакое значение есть\n")
                    continue
                self.list.clear()

                with open("vocabulary.data", "wb") as f:

                    for a,s in self.list.items():
                        if a == self.askU3:

                            self.list[self.askU2] = s
                            pickle.dump(self.list, f)
                            self.list.clear()
                            print("\nУспешо исправлено")
                            self.list.clear()
                            break


            elif self.askU == 2:

                # На английском
                with open("vocabulary.data", 'rb+') as f:
                    self.list.update(pickle.load(f))

                self.askU3 = input("\nВведи редактируемое слово на Eng:\n-->")
                self.askU2 = input("\nВведи исправленный вариант\n--> ")

                # Проверка на существование значения в сохранении
                if os.path.getsize(self.adress[0]) > 0:
                    with open(self.adress[0], "rb+") as f:
                        self.list.update(pickle.load(f))
                        for i,s in self.list.items():
                            if self.askU2 == s:
                                self.askU4 = True
                                break

                if self.askU4:
                    print("\nТакое значение есть\n")
                    continue
                self.list.clear()


                with open("vocabulary.data", "wb") as f:

                    for a,s in self.list.items():
                        if s == self.askU3:

                            self.list[a] = self.askU2
                            pickle.dump(self.list, f)
                            self.list.clear()
                            print("\nУспешо исправлено")
                            self.list.clear()
                            break

            elif self.askU == 3:
                break
            else:
               print("Нет такой команды!")

    def Phrases_add(self):

        # Работа c фразами
        while True:

            self.askU3 = input("""
Введи команду:
1 - Запись фразы
2 - Работа с фразами
3 - Выход
-->""")

            # Проверка ввода пользователя
            self.askU = SkanIn(self.askU3)
            if self.askU:
                continue
            else:
                self.askU3 = int(self.askU3)


            # Обработка ввода пользователя и исполнение команды
            if self.askU3 == 1:
                # Запись фраз

                self.Rus = input("Фраза на Rus\n-->")
                self.Eng = input("Фраза на Eng\n-->")
                # Проверка на существование значения в сохранении
                if os.path.getsize(self.adress[2] ) > 0:
                    with open(self.adress[2], "rb+") as f:
                        self.list.update(pickle.load(f))
                        for i,s in self.list.items():
                            if self.Rus == i:
                                self.askU4 = True
                                break
                            if self.Eng == s:
                                self.askU4 = True
                                break


                if self.askU4:
                    print("\nТакое значение есть\n")
                    continue
                self.list.clear()


                self.list[self.Rus] = self.Eng

                if os.path.getsize("phrese_vb.data") > 0:

                    with open("phrese_vb.data", "rb+") as f:
                        self.list.update(pickle.load(f))

                    with open("phrese_vb.data", "wb") as f:
                        pickle.dump(self.list, f)
                    self.list.clear()
                else:
                    with open("phrese_vb.data","wb") as f:
                        pickle.dump(self.list, f)
                    self.list.clear()

            elif self.askU3 == 2:
                # Чтение словоря фраз или удалить
                if os.path.getsize("phrese_vb.data") == 0:
                    print("Словарь пуст")
                    continue
                self.askU = input("""
Введи команду:
1 - Читать фразы
2 - Удалить фразу
 3 - Выйти
-->""")
                # проверка ввода
                self.askU2 = SkanIn(self.askU)
                if self.askU2:
                    continue
                else:
                    self.askU = int(self.askU)

                # Выполнение команд
                if self.askU == 1:
                    # Чтение фразу
                    self.askU2 = input("Введи команду:\n1 - Читать все\n2 - Поиск по Rus\n3 - поиск по Eng\n4 - Выход\n-->")

                    self.askU = SkanIn(self.askU2)
                    if self.askU:
                        continue
                    else:
                        self.askU2 = int(self.askU2)

                    # Выполнение чтения
                    if self.askU2 == 1:
                        # Читать все
                        with open("phrese_vb.data", "rb+") as f:
                            self.list.update(pickle.load(f))
                            for i,s in self.list.items():
                                print("\n",i," == ",s)
                            self.list.clear()

                    elif self.askU2 == 2:
                        # Чтение по RUS
                        with open("phrese_vb.data", "rb+") as f:
                            self.list.update(pickle.load(f))
                            self.askU2 = input("Rus--> ")
                            for i,s in self.list.items():
                                if i == self.askU2:
                                    print("\n",i," == ",s)
                            self.list.clear()

                    elif self.askU2 == 3:
                        # Чтение по Eng
                        with open("phrese_vb.data", "rb+") as f:
                            self.list.update(pickle.load(f))
                            self.askU2 = input("Eng--> ")
                            for i,s in self.list.items():
                                if s == self.askU2:
                                    print("\n",i," == ",s)
                            self.list.clear()

                    elif self.askU2 == 4:
                        continue
                    else:
                        print("Неверная команда")

                elif self.askU == 2:
                    # Удаление фраз

                    with open("phrese_vb.data", "rb+") as f:
                        self.list.update(pickle.load(f))

                    with open("phrese_vb.data", "wb") as f:
                        self.askU2 = ("Введи удаляемую фразу:\n-->")
                        for i,s in self.list.items():
                            if i == self.askU2:
                                print(self.askU2, " удалено ", self.list.pop(self.askU,"Такого ключа нет"))
                            if s in self.askU2:
                                print(self.askU2, " удалено ", self.list.pop(i,"Такого ключа нет"))
                        pickle.dump(self.list, f)
                    self.list.clear()
                elif self.askU == 3:
                    # Выход
                    break

                else:
                    print("Такой команды нет")

            elif self.askU3 == 3:
                # Выход
                break

            else:
                print("Нет такой команды")

    def Write_Text(self):
        # Запись текстов
        self.askU = True
        while self.askU:
            # Инструкция
            print("""
            Работа с текстами:
            1 - Читать тексты
            2 - Запись текста
            3 - Удаление текста
            0 - Выход
            """)

            # Проверка ввода пользователя
            self.askU2 = input("-->")
            self.askU3 = SkanIn(self.askU2)
            if self.askU3:
                continue
            else:
                self.askU2 = int(self.askU2)

            # Начало работы
            if self.askU2 == 1:
                # Чтение

                self.askU2 = input("Способ чтения:\n1 - Читать все\n2 - Поиск по названию\n3 - Выход\n-->")

                # Проверка ввода
                self.askU3 = SkanIn(self.askU2)
                if self.askU3:
                    continue
                else:
                    self.askU2 = int(self.askU2)

                # Выполнение чтения
                if self.askU2 == 1:
                    # Читать все
                    if os.path.getsize("text_book.data") == 0:
                        print("Фаил пуст")
                    else:
                        with open("text_book.data","rb+") as f:
                            self.list.update(pickle.load(f))
                            for i,s in self.list.items():
                                print(i)
                                print(s,"\n\n\n")
                            self.list.clear()
                elif self.askU2 == 2:
                    # Поиск по названию
                    if os.path.getsize("text_book.data") == 0:
                        print("Фаил пуст")
                    else:
                        self.askU3 = input("Введи название текста\n-->")
                        with open("text_book.data", "rb+") as f:
                            self.list.update(pickle.load(f))
                            for i,a in self.list.items():
                                if i == self.list:
                                    print(i,a)
                            self.list.clear()
                elif self.askU2 == 3:
                    # Выход
                    break
                else:
                    print("Нет такой команды")

            elif self.askU2 == 2:
                # Запись текста

                # Руская вариация текста
                while self.askU:
                    print("Водите текст до звездочки = * ")
                    self.Rus = input("RUS--> ")
                    self.Text = self.Text + ' ' + self.Rus
                    for i in self.Rus:
                        if i == "*":
                            self.Text = " RUS - " + self.Text[:-1] + "  "
                            self.Rus = ""
                            print("\n",self.Text,"\n")

                            while self.askU:
                                # Английская вариация текста
                                print("Водите текст до звездочки = * ")
                                self.Eng = input("ENG--> ")
                                self.Text2 =  self.Text2 + ' ' + self.Eng
                                for i in self.Eng:
                                    if i == "*":
                                        self.Text2 = "ENG - " + self.Text2[:-1]
                                        print(self.Text2)
                                        self.Text = self.Text + self.Text2
                                        self.askU3 = input("Введи название\n-->")
                                        self.askU = False
                                        self.list[self.askU3] = self.Text

                                        if os.path.getsize("text_book.data") > 0:
                                            with open("text_book.data","rb+") as f:
                                                self.list.update(pickle.load(f))

                                            with open("text_book.data", "wb") as f:
                                                pickle.dump(self.list,f)
                                            self.list.clear()

                                        else:
                                            with open("text_book.data","wb") as f:
                                                pickle.dump(self.list,f)
                                            self.list.clear()

            elif self.askU2 == 3:
                # Удаление
                self.askU3 = input("Введи название текста\n-->")
                with open("text_book.data", "rb+") as f:
                    self.list.update(pickle.load(f))
                    for i,a in self.list.items():
                        if i == self.askU3:
                            print("\nУдалено: ", self.askU3, " - ",self.list.pop(self.askU3," Такого ключа нет"))
                            break
                with open("text_book.data",'wb') as f:
                    pickle.dump(self.list,f)
                self.list.clear()

            elif self.askU2 == 0:
                # Выход
                break
            else:
                print("Нет такой команды")


    def Del_word(self):
        # Удаление

        while True:

            # Проверка на наличее данных в файле для корекной работы программы
            if os.path.getsize("vocabulary.data") == 0:
                print("\nСловарь пуст\n")
                break

            # Ввод пользователя
            self.askU = input("\nВыберите способ удаления:\n1 - Удалить по Рус\n2 - Удалить по Eng\n3 - Удалить все\n0 - Выход в основное меню\n-->")

            # Проверка ввода пользователя
            self.askU2 = SkanIn(self.askU)
            if self.askU2:
                continue
            else:
                self.askU = int(self.askU)

            # Обработка ввода пользователя и выполнение инструкций
            if self.askU == 1:
                # Удаление по ключу
                self.askU3 = input("\nВведи на Рус\n-->")

                with open(self.adress[0], "rb+") as f:
                    self.list.update(pickle.load(f))
                for a,s in self.list.items():
                    if a == self.askU3:
                        print("\nУдалено: ", self.askU3, " - ",self.list.pop(self.askU3," Такого ключа нет"))

                        with open("vocabulary.data", 'wb') as f:
                            pickle.dump(self.list,f)
                        self.list.clear()

                        break



            elif self.askU == 2:
                # Удаление по значению
                self.askU3 = input("\nВведи на Eng\n-->")

                with open(self.adress[0], "rb+") as f:
                    self.list.update(pickle.load(f))
                for a,s in self.list.items():
                    if s == self.askU3:
                        print("Удалено",self.askU3, '-',self.list.pop(a,"Нет такого значения\n"))

                        with open(self.adress[0], 'wb') as f:
                            pickle.dump(self.list,f)
                        self.list.clear()

            elif self.askU == 3:
                # Удаление всего
                with open("vocabulary.data", 'wb') as f:
                    print("\nВсе удалено\n")

            elif self.askU == 0:
                # Выход в главное меню
                print("\nВыход в основное меню\n")
                break

            else:
                print("\nНет такой команды\n")






go_WV = Work_vocablary()




while True:
    # Начало работы с пользователем

    if instructions:
        # Проверка запуска обучения
        seyHi()
    else:
        print("\n9 - Повториь инструкцию\n")

    # Проверка ввода пользователя
    user_input = input("Введи команду\n-->")
    skanout = SkanIn(user_input)
    if skanout:
        continue
    else:
        comand_user = int(user_input)


    # Обработка ввода пользоватея
    if comand_user == 0:
        print("""Вы уверены что хотите завершить работу с словарем?""")
        exit = input("-->")
        if exit == "":
            break
        else:
            continue

    elif comand_user == 1:
        # Запись в словарь
        go_WV.Write()

    elif comand_user == 2:
        # Чтение словаря
        go_WV.Read()

    elif comand_user == 3:
        # Редактирование словаря
        go_WV.Edit_vc()

    elif comand_user == 4:
        # Работа с текстом и преводом
        go_WV.Write_Text()

    elif comand_user == 5:
        # Работа с фразами
        go_WV.Phrases_add()

    elif comand_user == 6:
        # Удаление из словаря
        go_WV.Del_word()

    elif comand_user == 9:
        # Вывод инструкции
        instructions = True

    else:
        print("\nТакой команды нет!\n")





askU_copi = input("Выполнить резервное копирование:\n1 - Да\n0 - Нет\n-->")

instructions = SkanIn(askU_copi)
if instructions:
    pass
else:
    askU_copi = int(askU_copi)

if askU_copi == 1:


    list_adress = ("vocabulary.data",
                   'text_book.data',
                   'phrese_vb.data')
    list_adrCopi = ('copi_vocabu.data',
                    'copi_TextBook.data',
                    'copi_phrVb.data')
    nam = 0
    for i in list_adress:
        s = list_adrCopi[nam]
        nam += 1

        # Запись в фаил резервного копирования
        load = None# выгруска с сохранения
        load2 = None# выгрузка с резервной копии

        if os.path.getsize(i) > 0:
            if os.path.getsize(s) > 0:
                # Выполняется при писудствии данных в обоих файлах
                with open(i,"rb+") as f:
                    load = pickle.load(f)
                with open(s,"rb+") as f:
                    load2 = pickle.load(f)

                load2.update(load)

                with open(s,"wb") as f:
                    pickle.dump(load2, f)

            else:
                # Выполняется если сохранения пусты
                with open(i,"rb+") as f:
                    load = pickle.load(f)

                with open(s,"wb") as f:
                    pickle.dump(load, f)



elif askU_copi == 0:
    print("See you))")
else:
    print("Введено не верное значение\n\nПрограмма завершина")
