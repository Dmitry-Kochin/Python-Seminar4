'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.'''
a = set([int(x) for x in input('Введите элементы набора 1 через пробел: ').split()])
print(a)
b = set([int(x) for x in input('Введите элементы набора 2 через пробел: ').split()])
print(b)

c = set.intersection(a,b)
c = list(c)
c.sort()

print('Элементы пересечения:',c)