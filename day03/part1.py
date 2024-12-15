import re

file = open("./day03/input.txt", "r")
input_str = file.read()

mult_strs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_str)
answer = sum(int(a) * int(b) for a, b in mult_strs)

print(answer)
