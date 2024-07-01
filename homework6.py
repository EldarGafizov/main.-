my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Masha'])
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
print(my_dict)
del my_dict['Egor']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'Яблоко', 42.314}
print(my_set)
my_set.update({15, 1.6})
print(my_set)
my_set.discard(42.314)
print(my_set)

