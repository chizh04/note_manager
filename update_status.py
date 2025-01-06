input_status = ["Отложено"] # статус заметки. Меняется в результате работы программы на основе ввода данных пользователем

dict_status = ["Отложено", "Выполнено", "В работе"] # Возможные варианты статуса заметки.

print("Текущий статус заметки:", input_status[0], "\n")
print("Возможные статусы заметки: \n"
      " 1. Отложено \n"
      " 2. Выполнено \n"
      " 3. В работе \n")

# Функционал для изменения пользователем статуса заметки:
while True:
    status = input("Введите новый статус заметки из возможных (или его порядковый номер): ")
    if status == "1" or status == "Отложено" or status == "отложено":
        status_ = dict_status[0]
        input_status[0] = status_
        break
    elif status == "2" or status == "Выполнено" or status == "выполнено":
        status_ = dict_status[1]
        input_status[0] = status_
        break
    elif status == "3" or status == "В работе" or status == "в работе":
        status_ = dict_status[2]
        input_status[0] = status_
        break
    else:
        input("Недопустимый статус заметки, повторите ввод: ")

actual_status = {"status" : input_status[0]}

# Вывод нового статуса заметки:
print("Статус заметки успешно изменен на: ")
print(actual_status["status"])