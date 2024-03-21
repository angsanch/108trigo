##
## EPITECH PROJECT, 2023
## parse.py
## File description:
## parse information
##

import sys
import math

def check_matrix():
    data = []
    for i in range(len(sys.argv) -2):
        data.append(int(sys.argv[i + 2]))
    if (math.sqrt(len(data)) % 1) == 0:
        return data
    raise ValueError("Incorrect number of coeficients")
        

def check_function():
    functions = ["EXP", "COS", "SIN", "SINH", "COSH"]
    for i in range(len(functions)):
        if functions[i] == sys.argv[1]:
            return functions[i]
    raise Exception("Unrecognized function to be applied.")

def parse_data():
    data = {
        "func": check_function(),
        "matrix": check_matrix(),
    };
    return data