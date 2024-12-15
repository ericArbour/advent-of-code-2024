file = open("./day02/input.txt", "r")

input_str = file.read()
lines = input_str.splitlines()
reports = (list(map(int, line.split())) for line in lines)

safe_count = 0

for report in reports:
    last_diff = None
    for index, level in enumerate(report):
        if index == 0:
            continue

        diff = level - report[index - 1]
        local_last_diff = last_diff
        last_diff = diff

        if local_last_diff != None and (local_last_diff > 0) != (diff > 0):
            break

        step = abs(diff)
        if step < 1 or step > 3:
            break

        if index == len(report) - 1:
            safe_count += 1

print(safe_count)
