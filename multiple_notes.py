from datetime import datetime

# функция для проверки даты создания на соответствие формату и добавления ее в переменную для списка
def add_created_date():
    created_date = "i"
    created_date_ = input("Введите дату создания заметки в формате дд-мм-гггг: ")
    try:  # проверка дат на соответсвтие формату
        created_date = datetime.strptime(created_date_, format("%d-%m-%Y"))
    except ValueError:
        while created_date == "i":
            created_date_ = input("Вы ввели дату в не верном формате, введите снова: ")
            try:
                created_date = datetime.strptime(created_date_, format("%d-%m-%Y"))
            except ValueError:
                created_date = "i"
    return created_date

# функция для проверки дедлайна на соответствие формату и добавления его в переменную для списка
def add_deadline():
    deadline = "i"
    deadline_ = input("Введите срок исполнения заметки в формате дд-мм-ггг: ")
    try:
        deadline = datetime.strptime(deadline_, format("%d-%m-%Y"))
    except ValueError:
        while deadline == "i":
            deadline_ = input("Вы ввели дату в не верном формате, введите снова: ")
            try:
                deadline = datetime.strptime(deadline_, format("%d-%m-%Y"))
            except ValueError:
                deadline = "i"
    return deadline


print("Добро пожаловать в \"менеджер заметок\"! ")

notes = {}  # Словарь для сохранения заметок

# Промежуточные переменные для работы программы:
quantity_notes = len(notes)
quantitu_titles = 0
x = 0
# Основной цикл для создания заметок:
while x == len(notes):
    title = input("Ведите заголовок заметки: ")
    while quantitu_titles == len(notes):
        if title in notes.keys():  # Проверка на уникальность заголовков
            title = input("Такая заметка уже существует, повторите ввод: ")
        else:

            name = input("Введите Ваше имя: ")

            content = input("Введите описание заметки: ")

            status = input("Введите статус заметки: ")

            created_date = add_created_date()

            deadline = add_deadline()

            quantitu_titles = quantitu_titles + 1
    key_ = x + 1
    notes[key_] = [name, title, content, status, created_date, deadline]
    # Запрос на добавление еще одной заметки:
    while True:
        Add_ = input("Вы желаете добавить еще одну заметку? ")
        if Add_.lower() == "да":
            x = x + 1
            break
        elif Add_.lower() == "нет":
            break
        else:
            print("Ваш ответ не ясен, повторите ввод")

print("Список заметок: ")
notes_list = notes.keys()
for i in notes_list:
    print("    Имя пользователя:", notes[i][0], "\n"
          "    Заголовок заметки:", notes[i][1], "\n"
          "    Описание заметки:", notes[i][2], "\n" 
          "    Статус:", notes[i][3], "\n"
          "    Дата создания заметки:", str(notes[i][4])[:10], "\n"
          "    Срок исполнения:", str(notes[i][5])[:10], "\n"
          )

