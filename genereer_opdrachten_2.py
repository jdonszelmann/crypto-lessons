#!/usr/bin/env python3
import random, sys

woorden = list({
    "aan",
    "een",
    "oom",
    "voor",
    "roof",
    "doof",
    "oor",
    "door",
    "laat",
    "naar",
    "haar",
    "heer",
    "hoor",
    "koor",
    "aap",
    "jaap",
    "raap",
    "kaap",
    "ree",
    "een",
    "nee",
    "kaal",
    "raad",
    "taal",
    "baal",
    "duur",
    "huur",
    "puur",
    "kuur",
    "keel",
    "deel",
    "veel",
    "aal",
    "paar",
    "daar",
    "leer",
    "peer",
})

from crypto.genereer_opdrachten_1 import lookup, rotate_list, rotate_text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        num_leerlingen = int(sys.argv[1])
    else:
        num_leerlingen = int(input("hoeveel leerlingen? "))

    for i in range(num_leerlingen):
        rotate_numer = random.randint(10, len(lookup) - 5)
        offset_table = rotate_list(lookup, rotate_numer)
        text = random.choice(woorden)
        offset_text = rotate_text(offset_table, lookup, text)

        if offset_text in woorden:
            print(offset_text)
            continue

        print(" ".join([f"{ord(i):03}" for i in offset_text]))
        # print("".join([f"{i}" for i in offset_text]))