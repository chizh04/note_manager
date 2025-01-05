add_titles = [] # переменная для создания списка заголовков, введенных пользователем

# цикл для добавления заголовков, введенных пользователем в список:
while True:
    title_ = input("Введите название заголовка (или оставьте пустым для завершения): ")

    # Проверяем ввденный заголовок на уникальность:
    for i in add_titles:
        if i == title_:
            title_ = input("Такой заголовок уже существует, введите другое название (или оставьте пустым для завершения): ")

    if title_ == "":
        break
    add_titles.append(title_)

titles = add_titles
# Функционал вывода ранее введенных заголовков на экран:
print("Заголовки заметки: ")

for i in titles:
    print("- ", i)