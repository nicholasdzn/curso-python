"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.7]
#      -  6    5    4    3    2    1
lista[5]='Outra coisa'


l1 = [1,2,3,4,5,6,8,9,10]


l1.extend('c')
l1.insert(0, 'lebron')
del(l1[3:6])

print(l1)
print(l1[-1])
print(l1[0])