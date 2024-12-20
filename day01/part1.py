file = open("./day01/input.txt", "r")

input_str = file.read()
lines = input_str.splitlines()
rows = (map(int, line.split()) for line in lines)
sorted_columns = [sorted(column) for column in zip(*rows)]
pairs = zip(*sorted_columns)
diffs = (abs(a - b) for a, b in pairs)
answer = sum(diffs)
print(answer)
