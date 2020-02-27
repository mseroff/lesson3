#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='UTF-8') as my_file:
    content = my_file.read()
    long_of_content = len(content)
    count_of_words = len(content.split())
    new_content = content.replace('.','!')

    print(long_of_content)
    print(count_of_words)

with open('referat2.txt','w',encoding='UTF-8') as my_new_file:
    my_new_file.write(new_content)


