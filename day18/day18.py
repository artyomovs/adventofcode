"""Advent of Code. Day 18: Operation Order."""
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

s = 0
i = 0
for line in lines:
    line = line.replace(' ', '').strip()

    # calculate without parentheses
    def calculate(line):
        # print(f"calculate line = {line}")
        if not(re.search(r'[\+\*]', line)):
            return line

        # find first expression, replace with calculation
        expression = re.search(r'\d+[\+\*]\d+', line).group(0)
        result = eval(expression)
        # print(f"expression = {expression} result = {result}")
        line = line.replace(expression, str(result))
        return calculate(line)


    # first - calculate inside parentheses
    def replace_parentheses(line):
        # print(f"line={line}")
        if not(re.search(r'[\(\)]', line)):
            return calculate(line)

        expression = re.search(r'\(([0-9 +*]+)\)', line).group(1)
        result = calculate(expression)
        line = line.replace(f"({expression})", str(result))
        return replace_parentheses(line)

    a = int(replace_parentheses(line))
    s = s + a
    i += 1
    print(f"{i} line = {line} sum = {a} total = {s}")
    print('\n')

print(f"total = {s}")
        

