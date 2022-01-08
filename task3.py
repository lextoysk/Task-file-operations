file = open('123.txt', 'tw', encoding='utf-8')
file.close()

def count():
    line_count = 0
    for line in myfile:
        line_count += 1
    return (line_count)

with open('1.txt', 'r', encoding='utf-8') as myfile:
    file1 = count()
with open('2.txt', 'r', encoding='utf-8') as myfile:
    file2 = count()
with open('3.txt', 'r', encoding='utf-8') as myfile:
    file3 = count()
file_size = {'1.txt': file1, '2.txt': file2, '3.txt': file3}
size_sorted = sorted(file_size.items(), key=lambda x: x[1])
with open('123.txt', 'a+', encoding='utf-8') as mynewfile:
    all_lines = file1 + file2 + file3
    for keys, items in size_sorted:
        mynewfile.write(keys+'\n')
        mynewfile.write(str(items)+'\n')
        with open(keys, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                mynewfile.write(line)
                if not line:
                    break
        mynewfile.write('\n')
