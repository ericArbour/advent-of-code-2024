file = open("./day02/sample.txt", "r")

input_str = file.read()
lines = input_str.splitlines()
reports = (list(map(int, line.split())) for line in lines)

safe_count = 0

for report in list(reports)[3:4]:
    print(report)
    last_diff = None
    has_one_unsafe = False
    for index, level in enumerate(report):
        if index == 0:
            continue

        diff = level - report[index - 1]
        local_last_diff = last_diff
        last_diff = diff

        if local_last_diff != None and (local_last_diff > 0) != (diff > 0):
            print('hit inc/dec issue')
            if has_one_unsafe:
                break
            has_one_unsafe = True
            continue

        step = abs(diff)
        if step < 1 or step > 3:
            print('hit step too big')
            if has_one_unsafe:
                break
            has_one_unsafe = True
            continue

        if index == len(report) - 1:
            safe_count += 1

print(safe_count)
