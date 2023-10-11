import random
def get_first_name():
    first_names=["Alice", "Bob", "David"]
    return random.choice(first_names)

def get_last_name():
    last_names=["Smith", "Jhonson", "Brown", "Davis"]
    return random.choice(last_names)
def get_numb():
     numb=[1,2,3,4,5,6,7,8,10]
     return random.choice(numb)
# print(type(numb))
# def get_full_name():
#     first = get_first_name()
#     last = get_last_name()
#     numb=get_numb()
 # return f"{first} {'_'} {numb} {last}"