from pprint import pprint

def read_file(file_path, file_path2, file_path3):
    result_list = []
    for lines in (file_path, file_path2, file_path3):
        with open(lines, 'r', encoding='utf-8') as file:
            liness = [line.strip() for line in file]
            numbers_of_lines = 0
            new_list = []
            for _ in liness:
                numbers_of_lines += 1
            new_list += (lines), numbers_of_lines, ''.join(liness)
        result_list.append(new_list)
    sorted_list = sorted(result_list, key=lambda x: x[1])
    return sorted_list

# pprint(read_file('1.txt', '2.txt', '3.txt'))

def write_file(file):
    with open('4.txt', 'w', encoding='utf-8') as file:
        for value in all_in_one:
            file.writelines('\n'.join(map(str, value)))
            file.writelines('\n')


all_in_one = read_file('1.txt', '2.txt', '3.txt')

write_file(all_in_one)