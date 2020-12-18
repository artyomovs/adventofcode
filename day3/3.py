from pprint import pprint

lines = list()

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

pprint(lines)

width = len(lines[0])
height = len(lines)

routes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def get_next_spot(x, y, route):
    y = y + route[1]
    x = x + route[0]
    if x > width:
        x = x % width
    return x, y

x = 1 
y = 1

all_trees = 1


# print(lines[0])
for route in routes:
    trees = 0
    print('-------------')
    print(f"dx = {route[0]} dy = {route[1]}\n")
    y = route[1]
    x = 1
    j = 0
    lines_new = list(lines)
    for line in lines[1:]:
        s = line        
        if (j + 1) % (route[1]) == 0:    
            x, y = get_next_spot(x, y, route)
            s = line[:x - 1] + "O" + line[x:] 
            if line[x - 1] == "#":
                trees += 1
                s = line[:x - 1] + "X" + line[x:]                
        lines_new[j + 1] = s
        j = j + 1
    all_trees = all_trees * trees
    pprint(lines_new)    
    print(f"dx = {route[0]} dy = {route[1]} trees = {trees} all_trees = {all_trees}")
    

print(all_trees)
