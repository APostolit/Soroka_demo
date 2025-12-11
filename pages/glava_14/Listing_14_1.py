# Листинг 14.1
# Записать информацию в файл
text = 'У лукоморья дуб зелёный;\n'\
'Златая цепь на дубе том:\n' \
'И днём и ночью кот учёный\n'\
'Всё ходит по цепи кругом;'
file_txt = open('my_file.txt', 'w')
file_txt.write(text)
file_txt.close()

# Прочитать информацию из файла
with open('my_file.txt', 'r') as file_txt:
    data_text = file_txt.read()

# Вывести содержимое файл
for line in data_text.splitlines():
    print(line)