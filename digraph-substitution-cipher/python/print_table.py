"""
Teo Honda-Scully | 2022

Prints a GH Markdown formatted ciphertext table that can be pasted into an MD file.
"""

import main

alpha = main.alpha
shift_row = main.shift_row
shift_column = main.shift_column
shift_alpha = main.shift_alpha

sbox = [[shift_alpha(alpha, shift_column)[i] + (shift_alpha(alpha, shift_row)[j])
         for j in range(len(alpha))] for i in range(len(alpha))]

# Everything local inside function so that it can be imported if needed.
def get_table():
    table = "|  |"
    t = "|  | 0 |\n| :---: | :---: |\n| 0 |  |"
    for i in range(1, len(alpha) + 1):
        table += " %s |" % i
    table += "\n"
    for i in range(1, len(alpha) + 2):
        table += "| :---: "
    for j in range(1, len(alpha) + 1):
        table += "\n| %s |" % j
        for i in range(1, len(alpha) + 1):
            table += " `%s` |" % sbox[j - 1][i - 1]
    return table

if __name__ == "__main__":
    print(shift_alpha)
    print(get_table())