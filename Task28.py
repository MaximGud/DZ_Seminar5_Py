# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input("Введите целое неотрицательное число А: "))
b = int(input("Введите целое неотрицательное число B: "))

def sum(a,b):
          
    if a>b:      
        if a==1: return b  
        summa = 1+ sum(a-1,b)
        return summa
    if b>a:
        if b==1: return a
        summa = 1+ sum(a,b-1)
        return summa 
    if b==a:
        if b==0 and a==0:return 0
        summa = 1+ sum(a-1,b-1)+1
        return summa
    
print(sum(a,b))