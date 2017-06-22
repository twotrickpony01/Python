import random, string

def pw_gen(n):
    poss_char = string.printable
    string_len = len(poss_char)
    empt_string = ""
    for i in range(0, n):
        empt_string += poss_char[random.randrange(0,string_len,1)]

    return empt_string

print pw_gen(int(raw_input("Please give a password length: ")))
