from collections import Counter

file = open("./day01/input.txt", "r")

input_str = file.read()
lines = input_str.splitlines()
rows = (map(int, line.split()) for line in lines)
columns = list(zip(*rows))
column1_counter = Counter(columns[1])
answer = sum(id * column1_counter[id] for id in columns[0])
print(answer)
