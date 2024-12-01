a = []
b = []

with open("numbers.txt", "r") as file:
    for line in file:
        columns = line.split()
        a.append(int(columns[0]))
        b.append(int(columns[1]))

a_sorted = sorted(a)
b_sorted = sorted(b)

abs_diff = [abs(a_sorted[i] - b_sorted[i]) for i in range(len(a_sorted))]

sum_diff = 0
for i in abs_diff:
    sum_diff += i

similarity = 0
for i in a:
    similarity += i * b.count(i)

print(sum_diff)
print(similarity)

