# Python. HW_1.
# Part_1

# 1) Создать переменную типа String
a= 'Veronika'
print(type(a), a)

# 2) Создать переменную типа Integer
b= 10
print(type(b),b)

# 3) Создать переменную типа Float
c=3.14
print(type(c),c)

# 4) Создать переменную типа Bytes
byte_type= bytes(127)
print(type(byte_type), byte_type)

# 5) Создать переменную типа List(список)
# последовательность элементов, разделенных между собой запятой и заключенных в квадратные скобки.изменяемый упорядоченный тип данных
l1=[12,13,20,17]
print(type(l1), l1)

# 6) Создать переменную типа Tuple(кортеж)
# последовательность элементов, которые разделены между собой запятой и заключены в скобки. неизменяемый упорядоченный тип данных
tuple1=('Veronika', 'Vika', 'Victor')
print(type(tuple1), tuple1)

# 7) Создать переменную типа Set(изменяемое неупорядоченное множество)
vlans = [10, 20, 30, 40, 100, 10]
set(vlans)
set1=set(vlans)
print(type(set1),set1)
# or
set2={'Minsk', 'Moskow','Riga'}
print(type(set2),set2)

# 8. Создать переменную типа Frozen set(неизменяемое множество)
ll2=[3.14, 34, 'Maria']
fr_set_type = frozenset(ll2)
print(type(fr_set_type), fr_set_type)

users = frozenset({"Anna", "Vova", "Alisa"})
print(type(users), users)

# 9) Создать переменную типа Dict(словарь)
# неупорядоченная коллекция пар «ключ — значение». пары элементов в форме ключ:значение в фигурных скобках
dict_type={'name':'Veronika',
           'age': 23,
           'location': 'Minsk'}
print(type(dict_type),dict_type)

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name= "Veronika"
surname="Koronets"
print('name + surname =', name + ' ' +surname)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name= "Veronika"
surname="Koronets"
print('name , surname =', name + ', ' +surname)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
location= 'Minsk'
temperature = 25
temp=str(temperature)
print('in '+ location +' today '+ 'is '+ temp)
# or
a="teacher is "
age= 32
print(a+ str(age) + ' years old')
# or
age = 23
message = "I am {} years old".format(age)
print(message)
# or
age = 25
message = f"He is {age} years old"
print(message)
# or
print(f"His age is {age}")

