# # LIST
# l1 = [1,2,3,4,5,6,7,44]
#
# # список строк
# l_names = ['Veronika', 'Bulka', 'Anna']
# print(l1)
# print(l_names)
#
# # пустой список. оба варианта
# l11 =[]
# l2 = list()
# print(l2)
#
# # список с разными типами данных
# obj_1 = [11,4,"Anna", True, ['', 'Ivan', 23], {"age": 30}]
# # обернуть список в список - выведет тоже самое, но ожидает только один список в скобках
# l22= [5,6,7,44]
# l23=list(l22)
# print(l22)
# print(l23)

# # выведет 5 раз значение 3. работает не только с числами
# l3= [3]
# l33= l3*5
# print(l33)
# l4=["Vasil", 'Anna', "Sergey"]
# l44=l4*5
# print(l44)

# # достать элемент списка по индексу. порядок начинается с 0
# l4=["Vasil", 'Anna', "Sergey"]
# l44_0=l4[0]
# l44_1=l4[1]
# l44_2=l4[2]
# print(l44_0)
# print(l44_1)
# # вызвать в обратном порядке. начинается с -1
# l44_n1=l4[-1]
# l44_n2=l4[-2]
# l44_n3=l4[-3]
# print(l44_n1)
# print(l44_n2)
# print(l44_n3)

# # замена значения списка. но добавить не получится
# l4=["Vasil", 'Anna', "Sergey"]
# l4[1] = 'Ira'
# n1,n2,n3 = l4
# print(l4)
# print(n1)
# print(n2)
# print(n3)
# # в переменные присовить эл-ты списка

# # итерирование списка.
# # перечислили элементы списка
# l4=["Vasil", 'Anna', "Sergey"]
# ll=len(l4)
# print(ll)

# # for i in l4:
# #      print(i)

# через цикл while
# i=0
# while i <len(l4):
#      print(l4[i])
#      i +=1

# PYTHON TUTOR: VISUALIZE CODE


# l1=["Vasil", 'Anna', "Sergey"]
# l2=["Vasil", 'Anna', "Sergey1"]

# # сравнение списков
# if l1==l2:
#     print('l1==l2')
#     print('l1=', l1)
#     print('l2=' ,l2)
# else:
#     print('NO l1 !=, l2')
#     print('l1=', l1)
#     print('l2=', l2)

# # добавление элементов в КОНЕЦ списка
# l1=["Vasil", 'Anna', "Sergey"]
# l2=["Vasil", 'Anna', "Sergey1"]
# print(l1)
# l1.append(1000)
# print(l1)
# n=0
# for i in l1:
#     l1.append(n)
#     print(l1)
#     n +=1
#     if len(l1) > 10:
#         break

# добавление на ВТОРУЮ позицию
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1)
# l1.insert(1,1000)
# print(l1)

# # добавление элементов (в конец)
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1)
# l1.extend([1,1000])
# print(l1)

# получение индекса элементов
# l1=["Vasil", 'Anna', "Sergey"]
# print('Anna', l1.index('Anna'))
# или
# for i in l1:
#     print(i, l1.index(i))

# # удаление по индексу
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1)
# l1.pop(1)
# print(l1)
# print('---')
# print(l1)
# l1.pop()
# print(l1)

# # удаление конкретных значений
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1)
# l1.remove('Vasil')
# print(l1)

# # удаление ВСЕХ значений
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1)
# l1.clear()
# print(l1)
#
# print(l1, len(l1))
# for i in range(0,10):
#     l1.append(i)
# print(l1, len(l1))

# # поиск по значению
# l1=["Vasil", 'Anna', "Sergey"]
# if "Sergey" in l1:
#     print("Sergey", "ok")

# # кол-во вхождений
# l1=["Vasil", 'Anna', "Sergey"]
# print(l1.count("Anna1"))

# # СОРТИРОВКА
# l1=["Vasil", 'Anna', "Sergey"]
# l1.sort()
# print(l1)
# # вывести в обратном порядке
# l1.reverse()
# print(l1)

# вывести максимальное значение
l1=["Vasil", 'Anna', "Sergey"]
l2 =[3,5,1,33,55,76,46,34,0,-1]
# print(max(l2))

# # два списка в один(=сложение)
# l3=l1+l2
# print(l3)

# l2.sort()
# # покажет список С 3 элемента
# print(l2)
# print(l2[3:])
# # покажет список ДО 5 элемента включительно
# print(l2[:5])
# # покажет список до -3 элемента
# print(l2[:-3])
# # покажет список от -3 элемента
# print(l2[-3:])
#
# # покажет список от 2 до 7 с шагом 2
# print(l2[2:7:2])

# отложенность
# вытащить элемент из списка
obj_1= [11,4,"Anna", True, ['', 'Ivan', 23], 11]
print(obj_1[4][1])
