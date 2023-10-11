# a = 10
# b = 5
#
# c1= a+b
# c2= a-b
# c3= a*b
# c4 = a/b

#c5-возвести в степень
# c5 = a**b

#c6-остаток от деления
# c6 = a%b
# c7 = [c1, c2, c3, c4, c5]
#
# print ("result1 = ", c1)
# print ("result2 = ", c2)
# print ("result3 = ", c3)
# print ("result4 = ", c4)
# print ("result5 = ", c5)
# print ("result6 = ", c6)
#
# for i in c7:
#     check = i % 2
#     if check ==0:
#         print ("even =", i)
#     else:
#         print ("odd =", i)

#операторы сравнения
# > < == >= <= !=(не равно)
#возвращают булевые Boolean значение (да, нет. истина или ложь - бинарный ответ)
# ctrl + / - "заморозить"

a1 = 10
a2 = 5
a3 = 15
a4 = 50
result = a1 < a2
print ("compare", a1,"<", a2)
print ("result = ", result)

result = a1 > a2
print ("compare", a1,">", a2)
print ("result = ", result)

result = a1 ==a2
print ("compare", a1, "==", a2)
print ("result =", result)

result = a1 != a2
print ("compare", a1, "!=", a2)
print ("result =", result)

result = a1 <= a2
print ("compare", a1, "<=", a2)
print ("result =", result)

#составные выражения. спрашивается несколько условий

#and or not
#
print ()
result2 = a1>a2 and a1>a3
r1=a1>a2
r2=a1>a3
print("R1=", r1)
print("R2=", r2)
print ("AND, OR, NOT --> Result = ", result2)

#если везде OR - хоть один true - будет true
#если везде and - хоть один false - будет false
print ()
result2 = a1==a2 or a1<a3
r1=a1==a2
r2=a1<a3
print("R1 a1==a2=", r1)
print("R2 a1<a3=", r2)
print ("R=", r1, r2)
print ("AND, OR, NOT --> Result = ", result2)

result2 = a1==a2 or a1<a3 and a1<a4
#false
#где and - объединяются и идут обособленно

print ()
#операторы ветвления IF
#в скобках д.б.TRUE, чтобы отработало print
# if False:
#     print ('item1')
# else:
#     print('item2')

if r1:
     print ('TRUE item1')
else:
     print('FALSE item2')

print ()
a1>10 or a1==10.
#если что-то верно, вернется TRUE
# if a1>10:
#     print ('TRUE item1')
# else:
#     print('FALSE item2')

#несколько возможных вариантов условий - elif
#что первое словили, остальные э-ты даже не стали прочитывать
print ()
if r2:
    print('TRUE item1')
    rr2 =a2**2
    if rr2==25:
        print ('RR2==', 25)

    print ('TRUE item1')
elif a1>a2:
    print('True item2')
elif a1==10:
    print('True item3')
else:
    print('FALSE item4')

print ()
if r2:
    print ('IF2 === r2', r2)
else:
    print ('IF2 ====== r2', r2)

print ()


