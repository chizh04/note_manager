username = input("Введите ваше имя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
title = [title1, title2, title3]
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Дата создания заметки в формате ДД-ММ-ГГГГ: ")
issue_date = input("Срок исполнения в формате ДД-ММ-ГГГГ: ")

print("Имя пользователя: ", username)
print("Заголовки заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date)
print("Дэдлайн: ", issue_date)