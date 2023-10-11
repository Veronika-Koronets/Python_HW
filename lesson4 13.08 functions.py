# # FUNCTIONS
ll = [11,22,33,44,55,66,77]
# def f1():
#     print('F1 Hello')
#
# for i in ll:
#     print('i=', i)
#     if i==44:
#         f1()

# для этой ф-ии надо 2 аргумента/параметра.ф-ия принимает на вход 2 парметра/аргумента(то, что в скобках)
# positional arguments. если мы обьявили ф-ию и указали по порядку аргументы это позиционирование...
# ..в каком порядке они указаны, в таком порядке они зайдут в ф-ю
# именнованные аргументы будут позже

# 1.  def f2(age,salary):
#     long_salary=age*salary
#     return long_salary
# если не пропишем return, будет NONE. если хотим куда-то потом вынести в консоль рез-т этой ф-ии надо return
# если дальше нигде не использовать а просто выводить рез-т в консоль, то можно просто print

# f2(2, 500)

# объявили переменную long_s и присвоили ей значение, кот.вернет ф-ия, когда её вызовут с такими параметрами(2, 500)
# long_s1 = f2(2, 500)
# long_s2 = f2(3, 500)
# long_s3 = f2(4, 600)
#
# sal_l= [long_s1, long_s2, long_s3]
# sal_l2=[f2(2, 500), f2(3, 500), f2(4, 600)]
# print('long_s =', sal_l)
# print('long_s =', sal_l2)
# # если какое-то значение пишем явно это хардкор. оно не зависит от входных параметров(напр. cc=1000)

# 2.
# def f2(salary_1, salary_2):
#     if type(salary_1) is str:
#         print('s1')
#         salary_1=int(salary_1)
#
#     if type(salary_2) is str:
#         print('s2')
#         salary_2=int(salary_2)
#     salary_2_months = salary_1+salary_2
#     return salary_2_months
# s1= 1000
# s2 = 1100
# result = f2(s1,s2)
# print(result)

# 2.1 засунем IFы в ф-ию
# def check_salary_1(salary_1):
#     if type(salary_1) is str:
#             print('s1')
#             salary_1 = int(salary_1)
#     return salary_1
#
# def check_salary_2(salary_2):
#     if type(salary_2) is str:
#             print('s2')
#             salary_2=int(salary_2)
#     return salary_2

# это внутрисозданная ф-ия
# def f2(salary_1, salary_2):
#     ss1=check_salary_1(salary_1)
#     ss2=check_salary_2(salary_2)
#
#     salary_2_months= ss1+ss2
#     return salary_2_months
# s1=1000
# s2='1300'
#
# result=f2(s1,s2)
# print(result)

# 3. если подаётся список
# def check_salary_1(s1):
#     if type(s1) is str:
#         print('s1')
#         s1 = int(s1)
#     return s1
# def f2(salary_1):
#     ss1=salary_1
#     result = 0
#     for i in salary_1:
#         result+= check_salary_1(i)
#     #     счетчик
#
#     return result
#
# ll=[1000,'2000','3000',4000]
# result=f2(ll)
# print(result)

# 3.1 ЗП за несолько месяцев
def check_salary_1(s1):
    if type(s1) is str:
        print('s1')
        s1 = int(s1)
    return s1
def f2(all_salaries):
    salary_sum =0
    # почему 0?
    for i in all_salaries:
        salary_sum += check_salary_1(i)

    months = str(len(all_salaries))
    #     счетчик
    result = 'your '+months+' months salary is ' + str(salary_sum) + '$'
    return result

ll=[1000, 2000,'3000',1000, 1500, 4000]
result=f2(ll)
print(result)