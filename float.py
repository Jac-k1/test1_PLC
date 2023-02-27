import re

regex = '([+-]?[0-9]*.[0-9]*|[0-9]+.)([Ee][+-]?[0-9]+)?[LlfF]?|[+-]?[0-9]+[eE][+-]?[0-9]+[LlfF]?'
'''
'[-+]?[0-9]+\.[a-zA-z0-9]*'
'''




def is_float(float):
    if re.fullmatch(regex, float):
        if float[-1] == 'l' or float[-1] == 'L':
            print(str(float) + " = this is a long double")
        elif float[-1] == 'f' or float[-1] == 'F':
            print(str(float) + " = this is a float")
        else:
            print(str(float) + " = this is double")
    
    else:
        print(str(float) + " = this is embarrassing mate XD")


float_1 = '15.75L'
float_2 = '-0.0025F'
float_3 = '15.75'
float_4 = '-2.5e-3F'
float_5 = '25E-4'

is_float(float_1)
is_float(float_2)
is_float(float_3)
is_float(float_4)
is_float(float_5)
