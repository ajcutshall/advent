from typing import List
safe_count = 0
dampened = 0


def test(numbers: List[int], initial: bool):
    global safe_count
    global dampened
    if (all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))) or (all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))):
        safe = []
        for i in range(len(numbers) - 1):
            val = abs(numbers[i] - numbers[i + 1])
            if val < 4:
                safe.append("true")
            else:
                safe.append("false")
        if "false" not in safe:
            if initial:
                safe_count += 1
            else: 
                dampened += 1
            return True


with open("numbers.txt", "r") as file:
    for line in file:
        numbers = [int(x) for x in line.split()]
        if not test(numbers, 1):
            i = 0
            while i < len(numbers):
                removed = numbers.pop(i)
                if test(numbers, 0):
                    break
                else:
                    numbers.insert(i, removed)
                    i += 1

print("Solution 1:", safe_count)
print("Solution 2:", safe_count + dampened)
