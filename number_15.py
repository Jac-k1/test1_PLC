import re

regex = '^[a-zA-Z_$][a-zA-Z_$0-9]*$'

def match(string): 
        if(re.fullmatch(regex, string)):
            print("it works as variable, method, or class")
        else:
              print("name no work m8")


line = '$valid'
line2 = '_thisworkstoo'
line3 = 'This_works_all_day'
line4 = '123invalid'

match(line)
match(line2)
match(line3)
match(line4)