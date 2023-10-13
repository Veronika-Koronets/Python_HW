# FOR, WHILE
#циклы
#написать кусок кода и чтобы повторился столько раз, сколько надо
#while. в скобках д.б. TRUE, чтобы работал
import time
# count =0
# while(True):
#     print(count)
#     count +=1
#     time.sleep(.500)
# #считает 500 мсек перед следующей итерацией

# count =0
# iter_count=1
# while(count<=10):
#     print(iter_count, '-- iter=', count)
#     if count == 5:
#      print('count ==', count)
#     count += 1
#     iter_count += 1
#     time.sleep(.200)

# count =0
# iter_count=1
# while(count<=10):
#     print(iter_count, '-- iter=', count)
#     if count == 5:
#      print('count ==', count)
#      break
#     count += 1
#     iter_count += 1
#     time.sleep(.200)

#итератор
ll = [11,22,33,44,55, ['qq','ww', 'tt','yy'], 66, 77]
# print(len(ll))
#len(ll) - длина списка

# count=0
# for i in ll:
#       print(count, ll[count])
#       count += 1
#       time.sleep(.200)

# count=0
# for i in range(0,len(ll)):
#     print(i, ll[i])
#     time.sleep(.200)

#если мы знаем, что 5-ый элемент списка - список
# for i in range(0,len(ll)):
#     print(i, ll[i])
#
#     if i==5:
#         for ii in ll[i]:
#             print('---', ii)

# for i in range(0,len(ll)):
#     print(i, ll[i], type(ll[i]))
#     if type(ll[i]) =='list':
#
#     # if len(i)!=1:
#          for ii in ll[i]:
#              print('---', ii)

# for i in range(0,len(ll)):
#      print(i, ll[i], type(ll[i]))
#      # if isinstance(ll[i], list):
#      #     for ii in ll[i]:
#      #         print('---', ii)
# #второй вариант
#      if type(ll[i]) is  list:
#          for ii in ll[i]:
#              print('---', ii)

#генератор имен

# import sys
# print(sys.path)
#
# sys.path.append("C:\kv\PycharmProjects\pythonProject1\lesson3 06.08 for, while.py")
import mymodyle
# mymodyle.get_first_name() зачем оно здесь?
for i in range(0,11):
    nn1 = mymodyle.get_first_name()
    nn2 = mymodyle.get_last_name()
    result= nn1+'_'+nn2
    print(i, result)

# (' +"'" + 'test1_' +nn1 + nn2+'@gmail.com' +"'"+')'+','

# sys.path.append('C:\kv\AppData\Local\Programs\Python\Python311\Lib\site-packages')
# import names
