import random, typing

#Agarra un elemento random de una lista
def pick_random_list(l: typing.List[any]) -> any:
    lenght = len(l)
    item = l[random.randint(0, lenght-1)]
    return item