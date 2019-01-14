__author__ = 'Забудкин С.А.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import math

num = input(" Please, input unsign number: ")
i = 0
maxValue=0
while i < len(num):
    if int(num[i]) > maxValue :
        maxValue = int(num[i])
    i += 1

print(" Max value " + str(maxValue))

maxValue=0
for s in num :
    if int(s) > maxValue :
        maxValue = int(s)

print(" Max value " + str(maxValue))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Please input number 1: ")
num1 = input("... ")

print("Please input number 2: ")
num2 = input("... ")

(num1,num2) = (num2, num1)
print(" num 1 : " + num1 + " num 2 : " + num2 )

num1 = int(num2) - int(num1)
num2 = int(num2) - int(num1)
num1 = num2 + num1

print(" num 1 : " + str(num1) + " num 2 : " + str(num2) )


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
varA = int(input("Please input a: "))
varB = int(input("Please input b: "))
varC = int(input("Please input c: "))

# at first find discriminant
# d=b^2-4ac
discriminant = varB*varB-4*varA*varC
# if D > 0
#x1 = (-b+math.sqrt(D))/2a
#x2 = (-b-math.sqrt(D))/2a
if discriminant > 0 :
    x1 = (-varB+math.sqrt(discriminant))/2*varA
    x2 = (-varB-math.sqrt(discriminant))/2*varA
    print(" discriminant = " + str(discriminant)  + " x1 = " + str(x1) + " x2 " +str(x2) )

    # if D == 0
    #x=-b/2a

elif discriminant == 0 :
    x = -varB/(2*varA)
    print(" discriminant = " + str(discriminant)  + " x = " + str(x)  )
elif discriminant < 0 :
    print(" discriminant = " + str(discriminant)  )







