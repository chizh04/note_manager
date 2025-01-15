notes = [{"Список покупок" : ["Алексей", "список покупок", "Купить товары на неделю"]}, #Список заметок
        {"Учеба" : ["Мария", "Учеба", "Подготовиться к экзамену"]}
        ]

# Функция для вывода заметок:
def printer_notes():
    global notes
    for i in range(len(notes)):
        j = notes[i]
        key_ = list(j.keys())

        print("    Имя пользователя:", j[key_[0]][0], "\n"
        "    Заголовок заметки:", j[key_[0]][1], "\n"
        "    Описание заметки:", j[key_[0]][2], "\n"
              )

print("Текущие заметки:")
printer_notes()

del_name = input("Введите заголовок или имя пользователя для удаления заметки: ") #Вводимый параметр для удаления

a = 0 #промежуточная переменная

for i in range(len(notes)): # цикл для проверки на наличие вводимого параметра в списке заметок
    j = notes[i]
    key_ = list(j.keys())
    note = j[key_[0]]
    a = 0
    for k in range(len(note)):
        if note[k] == del_name:
            notes.remove(j)
            print("Зметка успешно удалена. \n")
            a = 1
            break
        else:
            a = 0

    if a == 1:
        break

if a == 0:
    print("Такой заметки не обнаружено")
else:
    print("Остались следующие заметки: \n")
    printer_notes()
