# 1. Сгенерировать список из 500 Emails где каждый email заканчивается на @gmail.com текст
# до @gmail.com - символы (Латиница, цифры, _ . ) [user_29@gmail.com, alex.braun@gmail.com, …]

import mymodyle
for i in range(1,51):
    nn1 = mymodyle.get_first_name()
    nn2 = mymodyle.get_last_name()
    numb=mymodyle.get_numb()
    numb2=str(numb)
    result= nn1+'_'+nn2 +numb2+'@gmail.com'
    print(i, result)
# print(type(numb2))
# return f"{first} {'_'} {numb} {last}"


# 2. Преобразовать список Emails в Dict где ключ - это index элемента в списке
# 3. Создать список Name_Surname из 100 элементов, где каждое 10 имя “Adam”
# [“Adam_black”, “Olga_Savitskaya, …]
# 4. Создать список списков в котором будут пары
# [[“Adam_Black”, “Eva_Brain”], [], …]
# Этот список надо создать из списка в задании #3, в него должны войти все имена с фамилиями Adam-ов,
# парой для Адамав в каждом внутреннем списке должна быть Eva_фамилия
# [[“Adam_Black”, “Eva_Brain”], [], …]
#
# 5. Сгенерировать список из 100 кличек для животных , в списке должно быть 10 одинаковых кличек
# [“Spike”, “Barboss”, “Bloom”, “Spike”, …]
# 6. Найти дубликаты в списке кличек и удалить их из списка, оставив один экземпляр клички дубликатов.