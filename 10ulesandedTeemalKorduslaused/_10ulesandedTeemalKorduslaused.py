﻿import random
import os 
 

#1.1.    Вводят 15 чисел. Определить, сколько среди них целых.


print("***  Введите 15 чисел. Я определю, сколько среди них целых.  ***\n") #print() выводит предложение в консоль
t=0
for i in range(15): #можно (1,16), вместо {i+1} и просто оставить {i}
    arv=float(input(f"Введите {i+1}. число\t")) #число с плавающей точкой
    if arv==int(arv):
        print(f"Число {arv} - целое")
        t+=1 #cчетчик введенных целых чисел
print()
print (f"Вы ввели {t} целых чисел.\n")


#2.2.    Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

print()
print("***  Сейчас мы найдем сумму всех натуральных чисел от 1 до числа введенное Вами!  ***\n")
a=int(input("Введите число: "))
summ=0 #Определяет переменную
if a<=0: #Если введённое число меньше или равно нулю, выдает сообщение об ошибке
    print("Вы ввели 0 или ненатуральное число")
else:
    for i in range (1, a+1): #Опеределяет размер массива требуемых данных(от 1 до введённого числа а+1)
        summ=i+summ #Ответ равен переменной summ + полученный ответ
    print(f"Сумма всех натуральных чисел с 1 до {a} равна {summ}")


#3.4.    Составьте программу, выводящую на экран квадраты чисел от 10 до 20.

print()
print("***  Сейчас мы вывидем на экран квадраты чисел от 10 до 20!  ***\n")

for i in range(10,21):
   print (f"{i} ** 2 = {i**2}")


#4.7.    Вывести на экран числа, кратные К из промежутка [А,В].

print()
print("***  Выводим на экран числа, кратные К из промежутка [А,В].  ***\n")
A=int(input("Введите наименьшее число для промежутка (A): ")) #Переменная
B=int(input("Введите наибольшее число для промежутка (B): ")) #Переменная
K=int(input("Введите кратное число для промежутка (K): ")) #Переменная
for i in range(A,B+1):
    if i%K==0: #деление с остатком
        print (f"{i} : {K} = {i%K}")


#5.8.    Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм = 2,5 см) для значений длин от 1 до 20 дюймов.

print()
print("***  Таблица перевода расстояний из дюймов в сантиметры, для значений длин от 1 до 20 дюймов.  ***\n")
for i in range(1,21): #Определяет размер массива данных от 1 до 21
   h=i*2.5 #Осуществляет перевод в дюймы путём умножения на 2,5
   print(f"{i} дюймов будет {h} в см ")


#6.9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

print()
print("***  В нашем банке трехпроцентный вклад.\nХотите узнать, какой станет сумма вклада через несколько лет?  ***\n")
i=int(input("На сколько лет делаем вклад? "))+1
s=int(input("Сколько кладем денег? "))
for i in range(1,i):
   s=s*1.03
   s=round(s,2) #округление до двух чисел после запятой
   print(f"Через {i} лет у вас будет {s}$")


#7.17. Напишите программу, печатающую столбик таблицу умножения такого вида: ---

print()
print("***  Столбик таблицы умножения  ***\n")
a=int(input("Какое число умножить от 1 до 10?\t"))

for i in range(1,10,1):
    print (f"{a} * {i} = {i*a}")




#8.19.    Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток 1, 2 или 5.

print()
print("***  Даны натуральные числа от 35 до 87.   ***\nВыведем те числа, которые при делении на 7 дают остаток 1, 2 или 5.\n")
for i in range(35,87): #Определяет размер массива данных от 35 до 87
   if(i % 7 == 1): 
       print(i)
   elif(i % 7 == 2):
       print(i)
   elif(i % 7 == 5):
       print(i)



#9.20.    Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.

print()
print("***  Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.  ***\n")
ans = 0 #Определяет переменную ans как 0
for i in range(1,50,1):
   if(i % 5 == 0): #Если деление без остатка на 5 равно 0, то переменная ans 
       ans += i #Прибавляет к переменной значение
   elif(i % 7 == 0): #Если деление без остатка на 7 равно 0, то к переменной прибавляется переменная i
       ans +=i
print(ans)


#10.22.    Найти сумму чисел от 100 до 200, кратных 17.

print()
print("***  Найти сумму чисел от 100 до 200, кратных 17.  ***\n")
ans1 = 0
for i in range(100,200):
   if(i % 17 == 0):
       ans1 += i
print(ans1)




"""
while 1:
    valik=int(input("Желаете перейти к следующему заданию? \n1 - Да \n0 - Нет \n"))

    if valik== '1':
        print("Идем дальше!")
    else:
        print('Выход..'.center(24, ' '))
        break




print("\nПереходим к следующему заданию! ")

valik=int(input("Желаете перейти к следующему заданию? \n1 - Да \n0 - Нет \n"))

if valik==1:
     os.system('CLS') 
else:
    exit()

print("Идем дальше!\n")

 









#9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
S=int (input("Введите сумму: "))
N=int (input("На сколько лет?  "))
St=Sw=S1=S
print("1. variant, for abil")
for i in range(N):
    S*=1.03
    print (f"{i+1} aasta lõpus summa = {S}")
print("2. variant")
S1=((1+3/100)**N)*S1
print (S1)
print("3. variant, while True abil")
i=0
while True:
    i+=1
    Sw*=1.03
    print (f"{i} aasta lõpus summa = {Sw}")
    if i==N: break
print(Sw)
print("4. variant, while tingimusega abil")
i=0
while i<N:
    i+=1
    St*=1.03
    print (f"{i} aasta lõpus summa = {St}")
  
print(St)


#3  Вводят 8 чисел. Найти их произведение (только положительных).
print("\nСейчас мы найдем произведение положительных чисел, введенные Вами!\n")
A=""
while type(A) != int:
    try:
        A=int(input("\nВведите любое число: "))
    except:
        TypeError
summa=1
for i in range(A): #1,2,3,4,5,6,7,8,9...A-1
    arv=float(input("Arv:"))
    if arv>0:
        print (f"{summa} * {arv} = {summa*arv}")
        summa*=arv
print(f"\nПроизведение положительных чисел равна: {summa}")
"""
