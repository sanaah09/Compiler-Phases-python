import re

KEYWORDS = {"int", "float", "char", "return"}

def lexical_analyzer(code):
    tokens = []
    words = code.replace(";", " ;").split()

    for word in words:
        if word in KEYWORDS:
            tokens.append(f"KEYWORD : {word}")
        elif word.isdigit():
            tokens.append(f"NUMBER : {word}")
        elif word in "=+-*/":
            tokens.append(f"OPERATOR : {word}")
        else:
            tokens.append(f"IDENTIFIER : {word}")

    return tokens

with open("input.txt") as f:
    code = f.read()

tokens = lexical_analyzer(code)

with open("output.txt", "w") as f:
    for t in tokens:
        f.write(t + "\n")
