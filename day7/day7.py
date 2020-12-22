"""Advent of Code 2020. Day 7: Handy Haversacks."""
import click
import re
from pprint import pprint

COLOR_NAME = "shiny gold"
COLORS_RESULTS = []
RESULT = 0


def get_bags_count(color, rules, part='1'):
    if part == '1':
        global COLORS_RESULTS
        for key, val in rules.items():
            if color in val:
                COLORS_RESULTS.append(key)
                get_bags_count(key, rules, part) 
    else:
        result = 0
        if len(rules[color].items()) == 0:
            print(f"{color} contain no other bags.")
            return 0
        else:
            for key, val in rules[color].items():      
                print(f"{color} contain {val} {key} bags.")                  
                result = result + val + val * get_bags_count(key, rules, part)
        return result        


        
            

@click.command()
@click.option('--part', type=click.Choice(['1', '2']), default='1', help="part 1 or 2")
def day7_main(part):
    rules = {}
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    if part == "1":
        # parse rules
        for line in lines:
            bag = line[:line.find("bags")].strip()
            inside_bags_list = re.findall(r'\d\s(.*?)\sbag', line)
            rules.update({bag:inside_bags_list})

        # count bags
        get_bags_count(COLOR_NAME, rules, part)

        # remove eual bags
        result = len(set(COLORS_RESULTS))
        print(result)
    else:
        # Part two
        for line in lines:
            bag = line[:line.find("bags")].strip()
            inside_bags = re.findall(r'\s(\d\s.*?)\sbag', line)
            rules.update({bag: {}})
            for inside_bag in inside_bags:
                count = int(inside_bag.strip()[:1])
                color = inside_bag.strip()[2:].strip()
                rules[bag].update({color:count})
        print('--------------')
        result = get_bags_count(COLOR_NAME, rules, part)
        print(f"result = {result}")


if __name__ == "__main__":
    day7_main()