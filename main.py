print(5 + 5)
print((type('hello world'))) # string - строчный тип данных
print('1' + '1')
print(type(True), type(False))
print(5 != 10 and 5<10)
print(type(str('5')))
print("Магистральный газопровод DN1400 PN 9.8Мпа (км 393,8 - 589,4)")
print(41*500-4500-9000)
print(5)
print(type(5))
print(5 + 5)
print(5 - 5)
print(5*5)
print(5/5)
print(5 // 5)
print(5%5)
print(5**5)
print(2.0)
print(type(2.0))
print(2.0 + 2.0)
print(2.0+2)
print('Hello, world')
print('Hello, world')
print(type('Hello, world'))
print('Hello,' + 'world')
print('1' + '1')
print('true', 'false')
print(type(True),type(False))
print(5>10)
print(10>5)
print(5==5)
print(5!=5)
print(5!=5 and 5<10)
print(5==5 and 5<10)
print(5!=5 or 5<10)
print(int('5'))
print(type(int('5')))
print(len('a'))
a = '1234'
s = sum(map(int, a))
print(s)
def f(x): return int (x) * 2
s = list(map(f, a))
print(s)

#Задача «Длина слова».
#Описание:
# Запишите в переменную a произвольную строку.
# Затем вычислите длину строки и выведите результат на экран(в консоль).
# для решения вам может пригодиться функция len(), которая позволяет определить длину строки.

a=('eldar')
print(len(a))


# Задача «Суммы и разности».Задача «Суммы и разности».
#Описание: запишите два целых числа в переменные first и second, вычислите их сумму и разность, запишите их в переменные summa и diff.
# Затем выведите значения переменных summa и diff на экран(в консоль) .

first = 10
second = 2
summa=(first+second)
diff=(first-second)
print(summa)
print(diff)

#Задача «Среднее арифметическое».
#Описание: Запишите три числа в переменные first, second и third соответственно и вычислите их среднее арифметическое, записав в переменную mean.
# Затем выведите значения переменной mean на экран(в консоль) .
first=1
second=2
third=3
mean=(first+second+third)
print(mean//3)

#Задача «Простые строчки».
#Описание: Создайте две переменных first_string и second_string и запишите в них строки "Вторник" и "Понедельник".
# Выведите на экран(в коносль) строки так, чтобы "Понедельник" шёл перед "Вторником" и между ними находилась запятая с пробелом (", ")
#Понедельник, Вторник

first_string="Вторник"
second_string="Понедельник"
print(second_string,first_string)

#Задача «Сложная формула».
#Описание:
# Запишите три числа в переменные a, b и c соответственно и создайте переменную f, в которую запишите результат выражения:
# (a * b) + (a * c).
# Возведите полученное число в третью степень и результат разделите(обычное деление) на два.
# Выведите его на экран(в консоль).

a=1
b=2
c=3
f=(a*b)+(a*c)**3//2
print(f)




