import click
import re
from pprint import pprint



ex_s = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}




@click.command()
@click.option('--part', type=click.Choice(['1', '2']), default='1', help="part 1 or 2")
def day6_main(part):
    with open('input.txt', 'r') as f:
        text = f.read()  

    if part == 1:      
        # Parse text into lists
        text = re.sub(r'\n\n', ',', text).replace('\n', '')
        answers = text.split(',')
        
        total = 0
        for a in answers:
            total = total + len(set(a))
        pprint(answers)
        print(total)
    else:
        total = 0
        text = re.sub(r'\n\n', ',', text).replace('\n', ';')        
        for group in text.split(','):
            s = ex_s
            persons = group.split(';')
            for person in persons:
                s = s & set(person)
            count_group = len(s)
            total = total + count_group
            print(f"group: {group} num: {total}")
        print(f"total = {total}")
            


if __name__ == "__main__":
    day6_main()