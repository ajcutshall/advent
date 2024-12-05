import re

def parse(content: list, to_find: str):
    count_found_row = 0
    count_found_col = 0
    count_found_diag_fwd = 0
    count_found_diag_back = 0
    content_rows = len(content)
    content_columns = len(content[0].strip())
    content_columns_list = [''] * content_columns

    for line in content:
        line = line.strip()
        fwd_match = re.findall(to_find, line)
        rev_match = re.findall(to_find[::-1], line)
        count_found_row += len(fwd_match) + len(rev_match)
        for i, char in enumerate(line):
            content_columns_list[i] += char

    for line in content_columns_list:
        fwd_match = re.findall(to_find, line)
        rev_match = re.findall(to_find[::-1], line)
        count_found_col += len(fwd_match) + len(rev_match)

    for di in range(-content_rows + 1, content_columns):
        diag = ''
        for row in range(content_rows):
            col = row + di
            if 0 <= col < content_columns:
                diag += content[row][col]
        fwd_match = re.findall(to_find, diag)
        rev_match = re.findall(to_find[::-1], diag)
        count_found_diag_fwd += len(fwd_match) + len(rev_match)

    for di in range(content_columns + content_rows - 1):
        diag = ''
        for row in range(content_rows):
            col = di - row
            if 0 <= col < content_columns:
                diag += content[row][col]
        fwd_match = re.findall(to_find, diag)
        rev_match = re.findall(to_find[::-1], diag)
        count_found_diag_back += len(fwd_match) + len(rev_match)

    count_found = (count_found_row + count_found_col + count_found_diag_fwd + count_found_diag_back)
    print("Part 1:", count_found)

with open("input.txt") as file:
    content = [line.strip() for line in file.readlines()]
    parse(content, "XMAS")