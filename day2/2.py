with open("input.txt", "r") as f:
    lines = f.read().splitlines()



a = []
for line in lines:
    s = {}
    s["min"] = int(line[:line.find("-")])
    s["max"] = int(line[line.find("-") + 1:line.find(" ")])
    s["char"] = line[line.find(" ") + 1:line.find(":")]
    s["text"] = line[line.find(":") + 2:]
    a.append(s)

count_all = 0
count_and = 0
for i in a:    
    text = i["text"]
    # text = text + "________________________________________________"
    # if len(text) > i["max"]:
    # if :
    #     count_and += 1
    left = text[i["min"] - 1]
    right = text[i["max"] - 1]
    char = i["char"]
    if (left == char or right == char) and not(left == char and right == char):
        print(f"{i['min']}-{i['max']} {i['char']}: {text}")
        count_all += 1
# count = count_all - count_and
print(count_all)
# print(count_and)
# print(count)







