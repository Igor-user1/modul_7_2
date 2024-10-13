def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        file.write(strings[i]+'\n')
    string_position = {}
    file = open(file_name, 'r', encoding='utf-8')
    file.seek(0)
    for j in range(len(strings)):
        a = file.tell()
        string_position[(j+1, a)] = strings[j]
        file.readline()
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
