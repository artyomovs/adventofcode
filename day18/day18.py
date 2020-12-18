"""Advent of Code. Day 18: Operation Order."""
import re
import click 

# calculate without parentheses
def calculate(line, part=1):
    # print(f"calculate line = {line}")
    if not(re.search(r'[\+\*]', line)):
        return line
    if part == 1:
        # find first expression, replace with calculation
        expression = re.search(r'\d+[\+\*]\d+', line).group(0)
    else:
        # find first expression, replace with calculation
        if re.search(r'\d+\+\d+', line):
            expression = re.search(r'\d+\+\d+', line).group(0)
        elif re.search(r'\d+\*\d+', line):
            expression = re.search(r'\d+\*\d+', line).group(0)

    result = eval(expression)
    line = line.replace(expression, str(result), 1)
    return calculate(line, part)        


# first - calculate inside parentheses
def replace_parentheses(line, part=1):
    if not(re.search(r'[\(\)]', line)):
        return calculate(line, part)

    expression = re.search(r'\(([0-9 +*]+)\)', line).group(1)
    result = calculate(expression, part)
    line = line.replace(f"({expression})", str(result))
    return replace_parentheses(line, part)



@click.command()
@click.option('--part', type=click.Choice(['1', '2']), default='1', help="part 1 or 2")
def day18_main(part):
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        line = line.replace(' ', '').strip()
        s = int(replace_parentheses(line, int(part)))
        total = total + s
        print(f"line = {line} sum = {s} total = {total}")
    print(f"total = {total}")        


if __name__ == "__main__":
    day18_main()