def print_params(a, b, c):
    print(a, b, c)

values_list = [1, True, 'stroka']
values_list_2 = [5, 'True', False]
values_dict = {'a': 1, 'b': 2, 'c': 5}
print_params(*values_list)
print_params(**values_dict)
#print_params(*values_list_2, 42) это не работает