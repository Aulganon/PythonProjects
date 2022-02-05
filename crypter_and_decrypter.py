# программа энигма она почти имитирует принцип работы реальной энигмы
# криптографическая стойкость данного пароля может быть невысокой
# в программе реализована псевдослучайная генерация паролей
# пользователю в данном случаее сообщаются пароли сгенерированные системой
# made by Pavel Tsikin 

# NOTE!!!!!!
# i don't care about right for this piece of sh*t
# all possible malfunctions or data losses is only on your responsibility
# this code can be used on your own risk XD
# Have fun and over :)

import random as rd
string = []
numb = []
max_numb_of_levels = 5
# максимальное кол-во перемешиваний определяемых функцией random
max_abs_number = 20
# максимальное значение сдвига в перемешивании определяемое функцией random

def main() :
    print("""Что вы хотите сделать?
    1 - зашифровать
    2 - расшифровать
    3 - случайная генерация чисел(вам будет выдано кол-во перемешиваний и пароли)
    P.S. В обоих случаях вам придётся ввести значения для кодирования/декодирования
        к тому же необходимо будет ввести фразу""")
    choice = int(input("Что мы выберем? = "))
    # спрашиваем пользователя о выборе номера в меню 
    if choice == 1 :
        action1()
    elif choice == 2:
        action2()
    elif choice == 3:
        action3()
    else:
        print("Такого значения нет в меню")

    
def action1():
    # функция кодирует слово из списка
    # по очереди перебирается массив(список) из букв
    # каждая буква переводится в номер позиции в unicode 
    # после этого складываются в int формате два числа   команда ord()
    # а затем переводится номер получившегося числа в символ unicode  команда chr()
    text = input("Введите строку, которую надо зашифровать\n")
    global string
    for char in text:
        string.append(char)
    global numb 
    print("Сколько уровней перемешивания мы хотим?")
    count_of_number = int(input())
    for i in range(count_of_number):
        print("Введите шифровальное значение №"+str(i)+" = ")
        lcl = int(input())
        numb.append(lcl)
        encrypt(i)
    print("Ваш результат равен = ",end= "")
    print(*string,sep="")
    input("\nНажмите enter, чтобы выйти")

def action2():
# тоже самое, что и action1(), но  для целей наоборот
    text = input("Введите строку, которую надо расшифровать\n")
    for char in text:
        string.append(char)
    global numb 
    print("Сколько уровней перемешивания у нас стоит?")
    count_of_number = int(input())
    for i in range(count_of_number) :
        print("Введите шифровальное значение №"+str(i)+" = ")
        lcl = int(input())
        numb.append(lcl)
    numb.reverse()
    for i in range (count_of_number):
        decrypt(i)
    print("Ваш результат равен = ",end= "")
    print(*string,sep="")
    input("\nНажмите enter, чтобы выйти")

def action3():
    text = input("Введите строку, которую надо зашифровать\n")
    global string
    for char in text:
        string.append(char)
    global numb 
    #берётся сид, по умолчанию сид системного времени
    rd.seed()
    # значение в диапазоне от 1 до макс числа перемешиваний
    level_en = rd.randint( 1 , max_numb_of_levels)
    print("Число перемешиваний = "+str(level_en))
    for i in range(level_en):
        # случайным образом пересчитывает значение от -макс до макс
        lcl = rd.randint(-max_abs_number ,max_abs_number)
        print("Шифровальное число №"+str(i)+" = "+ str(lcl))
        numb.append(lcl)
        # а дальше как в action1()
        encrypt(i)
    print("Ваш результат равен = ",end= "")
    print(*string,sep="")
    input("\nНажмите enter, чтобы выйти")

def decrypt(n) : 
    null = 0
    for i in string:
        unicode = ord(string[null])
        string[null] = chr(int(unicode) - numb[n] - null)
        null +=1

def encrypt(n) :
    null = 0
    for i in string:
        unicode = ord(string[null])
        string[null] = chr( int(unicode) + numb[n] + null )
        null +=1

main()
