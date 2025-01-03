username = input("Введите ваше имя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Дата создания заметки в формате ДД-ММ-ГГГГ: ")
issue_date = input("Срок исполнения в формате ДД-ММ-ГГГГ: ")

note = [
username,
content,
status,
created_date,
issue_date,
[title1, title2, title3]
]

print(note)