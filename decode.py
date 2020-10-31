#!/usr/bin/env python3

from genereer_opdrachten_1 import lookup, rotate_list, rotate_text

vowels = "eauoi"

def decipher(text):
    res = []
    for rotate_numer in range(len(lookup)):
        offset_table = rotate_list(lookup, rotate_numer)
        offset_text = rotate_text(lookup, offset_table, text)

        num_not_alpha = 0
        num_uncommon = 0
        capital = 0
        strange = 0
        numbers = 0
        numvowels = 0
        for i in offset_text:
            if not (i.isalpha() or i in "?!', "):
                num_not_alpha += 1
            if i.isdigit():
                numbers += 1
            if i in "qQxX":
                num_uncommon += 1
            if i.isupper():
                capital += 1
            if i in "{}[]%^\\|":
                strange += 1
            if i in vowels:
                numvowels += 1

        if num_not_alpha > (len(text) // 8) or num_uncommon > 3 or capital > (len(text) // 2) or strange > 1 or numbers > (len(text) // 4) or numvowels == 0:
            continue
        res.append(offset_text)

    return res


if __name__ == '__main__':

    while True:
        text = input("versleutelde tekst: ")
        print("\n".join(decipher(text)))
