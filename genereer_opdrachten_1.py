#!/usr/bin/env python3

import random
import sys

from regels import regels

lookup = [
    "SPACE",
    "!",
    "\"",
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    *[chr(i) for i in range(65, 91)],
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    *[chr(i) for i in range(97, 123)],
    "{",
    "|",
    "}",
    "~",
]


def rotate_list(seq, k):
    return seq[k:] + seq[:k]


def rotate_text(offset_table, lookup, text):
    offset_text = ""
    for letter in text:
        index = offset_table.index(letter if letter != " " else "SPACE")
        offset_text += lookup[index] if lookup[index] != "SPACE" else " "
    return offset_text


def rotate_text_by(rotate_numer, text):
    offset_table = rotate_list(lookup, rotate_numer)
    return rotate_text(lookup, offset_table, text)


def rotate_text_random(text):
    offset_table = rotate_list(lookup, random.randint(10, len(lookup) - 5))
    return rotate_text(lookup, offset_table, text)


def main():
    if len(sys.argv) > 1:
        num_leerlingen = int(sys.argv[1])
    else:
        num_leerlingen = int(input("hoeveel leerlingen? "))

    for i in range(num_leerlingen):
        rotate_numer = random.randint(10, len(lookup) - 5)
        offset_table = rotate_list(lookup, rotate_numer)

        text = random.choice(regels)

        offset_text = rotate_text(offset_table, lookup, text)

        print("binair,decimaal,letter,versleuteld")
        for index, name in enumerate(lookup):
            if name == "SPACE":
                i = 32
            else:
                i = ord(name)
            offset_name = offset_table[index].ljust(10, " ")
            name = name.ljust(10, " ")
            print(f"{i:08b},{i:03},{name},{offset_name}")

        #    print(text)
        print(offset_text)

        print("----------------------")

if __name__ == "__main__":
    main()



