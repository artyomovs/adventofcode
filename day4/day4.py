"""Day 4 of adventure of code. 
https://adventofcode.com/2020/day/4."""
from pprint import pprint
import re

passports = []
lines = []
valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parse_line(line):
    params = line.split(" ")
    dict_line = {}
    for param in params:
        key = param[:3]
        val = param[4:]
        dict_line[key] = val
    return dict_line

# Read
with open("input.txt", "r") as f:
    lines = f.readlines()

# Parse
passport = {}
for line in lines: 
    line = line.strip()
    if line == "":
        passports.append(passport)
        passport = {}
    else:
        passport.update(parse_line(line))

# pprint(passports)
# Analyze
valid_passports = 0
passport_after_1 = []
for passport in passports:
    p_keys = list(passport.keys())
    if 'cid' in p_keys:
        p_keys.pop(p_keys.index('cid'))
    if all(elem in p_keys for elem in valid_keys):
        print(passport)
        passport_after_1.append(passport)
        valid_passports+=1
print(valid_passports)



# Stage 2.
def is_valid(p):
    a = int(p['byr'])
    if a > 2002 or a < 1920:        
        return 0
    
    a = int(p['iyr'])
    if a > 2020 or a < 2010:        
        return 0      

    a = int(p['eyr'])
    if a > 2030 or a < 2020:
        return 0          

    a = int(p['hgt'][:len(p['hgt']) - 2])      
    b = p['hgt'][len(p['hgt']) - 2:]

    if (b == 'cm') and ( a < 150 or a > 193):
        return 0
    if (b == 'in') and ( a < 59 or a > 76):
        return 0

    a = p['hcl']
    b = a[1:]
    re_res = re.search(r'([0-9]|[a-f]){6}', b)

    if not re_res or a[:1] != "#":
        return 0

    a = p['ecl']
    if a not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0

    a = p['pid']
    if not (a.isnumeric() and len(a) == 9):
        return 0
    return 1


valid_passports_2 = 0
passport_after_2 = []

with open("output.txt", "w") as f:
    for passport in passport_after_1:
        if is_valid(passport) == 1:
            valid_passports_2+=1
            f.write(str(passport) + "\n")
            if passport not in passport_after_2:
                passport_after_2.append(passport)
                pprint(passport)
    
print(len(passport_after_2))