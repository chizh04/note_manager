username = input("Введите ваше имя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Дата создания заметки в формате ДД-ММ-ГГГГ: ")
issue_date = input("Срок исполнения в формате ДД-ММ-ГГГГ: ")

note = {
"username" : username,
"content" : content,
"status" : status,
"created_date" : created_date,
"issue_date" : issue_date,
"titles" : [title1, title2, title3]
}

print(note["username"])
print(note["content"])
print(note["status"])
print(note["created_date"])
print(note["issue_date"])
print(note["titles"])