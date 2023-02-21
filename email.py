import re

regex = '[a-zA-Z0-9.#%$&+*-/=?^_{|}!]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'


def is_email(email):
    if (re.fullmatch(regex, email)):
        print(str(email) + " = is email")
    else:
        print(str(email) + " = nah this aint it, chief")


email_1 = "yesiamemail@gmail.com"

email_2 = "?!?!?iamnotemail.com"

email_3 = "oh.boy.wo!uld.you@look-at--the.time.org"

is_email(email_1)
is_email(email_2)
is_email(email_3)
