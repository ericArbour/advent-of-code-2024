file = open("./day02/input.txt", "r")

input_str = file.read()
lines = input_str.splitlines()
reports = (list(map(int, line.split())) for line in lines)


def get_sub_reports(report):
    sub_reports = []
    for index, _ in enumerate(report):
        sub_reports.append(report[:index] + report[index + 1 :])

    return sub_reports


def is_sub_report_safe(report):
    sub_reports = get_sub_reports(report)
    for sub_report in sub_reports:
        if get_is_safe(sub_report, is_sub_report=True):
            return True

    return False


def get_is_safe(report, is_sub_report=False):
    last_diff = None
    is_safe = False
    for index, level in enumerate(report):
        if index == 0:
            continue

        diff = level - report[index - 1]
        local_last_diff = last_diff
        last_diff = diff

        if local_last_diff != None and (local_last_diff > 0) != (diff > 0):
            if is_sub_report:
                break
            return is_sub_report_safe(report)

        step = abs(diff)
        if step < 1 or step > 3:
            if is_sub_report:
                break
            return is_sub_report_safe(report)

        if index == len(report) - 1:
            is_safe = True

    return is_safe


safe_count = sum(1 for report in reports if get_is_safe(report))
print(safe_count)
