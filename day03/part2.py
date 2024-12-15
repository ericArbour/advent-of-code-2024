import re

ENABLE_TEXT = "do()"
DISABLE_TEXT = "don't()"

file = open("./day03/input.txt", "r")
input_str = file.read()


def get_mult_sums(section: str) -> int:
    mult_strs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", section)
    return sum(int(a) * int(b) for a, b in mult_strs)


def get_do_sections(section, do_sections):
    first_dont_index = section.find(DISABLE_TEXT)
    if first_dont_index == -1:
        return do_sections + [section]

    enabled_section = section[:first_dont_index]
    after_dont = section[first_dont_index + len(DISABLE_TEXT) :]
    after_dont_do_index = after_dont.find(ENABLE_TEXT)
    do_section = after_dont[after_dont_do_index:]
    return get_do_sections(do_section, do_sections + [enabled_section])


do_sections = get_do_sections(input_str, [])
answer = sum(get_mult_sums(section) for section in do_sections)

print(answer)
