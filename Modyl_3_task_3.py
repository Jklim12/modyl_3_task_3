def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a=2,b= 'string', c= False)
print_params( b=25 )
print_params(c= [1,2,3])
values_list = [1, 1.5, 'text']
values_dict = {'a':3,'b':6,'c':5}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1.2,'sun']
print_params(*values_list_2, 42)