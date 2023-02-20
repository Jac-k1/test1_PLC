import re

regex = '^[0-9a-fA-FxXiIlLuU]*'

def is_int(number):
    if(re.fullmatch(regex, number)):
        if number[0] == '0' and number[1] == 'x':
            print(str(number) + " = this is hexadecimal")
        elif number[0] == '0' and number[1] != 'x':
            print(str(number) + " = this is octal")
        else:
            print( str(number) + " = this is decimal")

        
    else:
        print(str(number) + " = what are you doing mate??")


number_1 = '28'
number_12 = '4000000024u'

number_2 = '024'
number_22 = '0200000000022l'

number_3 = '0x2a'
number_32 = '0x8a4400000000040Ui64'

number_wrong = '12.2'


is_int(number_1)
is_int(number_12)

is_int(number_2)
is_int(number_22)

is_int(number_3)
is_int(number_32)

is_int(number_wrong)