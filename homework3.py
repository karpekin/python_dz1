'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''
# from random import randint
# N = abs(int(input('Введите N: ')))
# A = [randint(1, N) for i in range(N)]
# print(A)
# X = abs(int(input('Введите X: ')))
# summ = 0
# for j in range(len(A)):
#     if A[j] == X:
#         summ += 1
# print(summ)
'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
'''
from random import randint
N = abs(int(input('Введите N: ')))
A = [randint(1, N) for i in range(N)]
print(A)
X = abs(int(input('Введите X: ')))

if max(A) >= X:
    mini = max(A)
else:
    mini = X

j = 0
for i in A:
    if abs(X-i) < mini:
        mini = abs(X-i)
        j = i
print(j)
