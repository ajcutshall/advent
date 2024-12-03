import re

with open ("input.txt", "r") as file:
    content = file.read()
    result_1 = 0
    result_2 = 0
    sanitized = []
    sanitized2 = []
    sanitized_list = re.findall(r'mul\([0-9]*,[0-9]*\)', content)
    for i in sanitized_list:
        sanitized.append(re.sub(r'\)', '', re.sub(r'mul\(', '', i)))
    for i in sanitized:
        mul = i.split(',')
        result_1 += int(mul[0]) * int(mul[1])
    list2 = re.findall(r"(?<=do\(\))((.|\n)*?)(?=don't\(\))", content)
    list2.append(re.findall(r"((.|\n)*?)(?=do\(\))", content)[0])
    flat_list2 = [i for ix in list2 for i in ix]
    sanitized_list2 = []
    for i in flat_list2:
        sanitized_list2.append(re.findall(r'mul\([0-9]*,[0-9]*\)', i))
    sanitized_list2 = [i for ix in sanitized_list2 for i in ix]
    for i in sanitized_list2:
        sanitized2.append(re.sub(r'\)', '', re.sub(r'mul\(', '', i)))
    for i in sanitized2:
        mul = i.split(',')
        result_2 += int(mul[0]) * int(mul[1])

    print(result_1)
    print(result_2)