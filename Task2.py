#  Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#  (т.е. не меньше заданного минимума и не больше заданного максимума)
 
import random
 
rand_list=[]
n= int(input("Введите длину массива: "))
for i in range(n):
    rand_list.append(random.randint(1,100))
print(rand_list)
 
num_min = int(input("Введите минимальное значение диапазона: "))
num_max = int(input("Введите максимальное значение диапазона: "))
 
list_ind = []
for i in range(len(rand_list)):
    if num_min <= rand_list[i] and rand_list[i]<= num_max:
        list_ind.append(i)
  
print("Индексы элементов заданного диапазона: ", list_ind) 