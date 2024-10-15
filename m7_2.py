def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        key = (i, file.tell())
        value = strings[i]
        strings_positions[key] = value
        file.write(strings[i])
        file.write('\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
print(custom_write('test.txt', info))