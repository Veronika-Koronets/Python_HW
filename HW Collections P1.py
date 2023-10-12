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
import mymodyle
for i in range(1,101):
    petname=mymodule.get_petname
    name_Sharik=['Sharik']
    result= petname +  name_Sharik*10
    random.shuffle(result)
    print(i, result)

2)
import random
name_Sharik=['Sharik']
petnames=['Spike', 'Barboss', 'Bloom', 'Kashtan']
result_names=[name_Sharik]*10+random.choice(petnames)
 random.shuffle(result_names)
print(i, result_names)

    
https://mooc.nspu.ru/pluginfile.php/33768/mod_resource/content/0/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87.pdf
# 6. Найти дубликаты в списке кличек и удалить их из списка, оставив один экземпляр клички дубликатов.
print(i, result)
result=list(set(result))

Это можно сделать путём преобразования списка во множество (set, иногда ещё его называют «набор»), а затем обратно в список:
https://skillbox.ru/media/code/spiski_v_python_11_voprosov_kotorye_mogut_zadat_na_sobesedovanii/
https://dzen.ru/video/watch/6011bef4814bd370b67ff17a?utm_referer=dzen.ru
