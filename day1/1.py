import pathlib


with open(f"{pathlib.Path(__file__).parent.absolute()}/input.txt", "r") as f:
    lines = f.read().splitlines()

numbers = list()
for line in lines: 
    numbers.append(int(line))

result = 0
numbers2 = list(numbers)
numbers3 = list(numbers)
for i in numbers:
    for j in numbers2: 
        for k in numbers3:
            if (i + j + k ) == 2020:
                print(f"i = {i} j = {j} k = {k}")
                result = i * j * k
                break

print(result)


