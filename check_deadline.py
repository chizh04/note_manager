from datetime import datetime, date

# Вывод на экран текущей даты:
today = datetime.today()
print("Сегодня", date.today())

# Модуль для получения даты дэдлайна от пользователя:
deadline = "i"
deadline_ = input("Введите срок исполнения заметки в формате дд-мм-гггг: ")

try:
    deadline = datetime.strptime(deadline_, format("%d-%m-%Y"))
except ValueError:
    while deadline == "i":
        deadline_ = input("Вы ввели дату в не верном формате, введите снова: ")
        try:
            deadline = datetime.strptime(deadline_, format("%d-%m-%Y"))
        except ValueError:
            deadline = "i"

# Сверка дат и вывод сообщения о скроках дэдлайна:
result = today - deadline
difference_days = result.days

while True:
    if difference_days == 0:
        print("Внимание! Сегодня истекает срок исполнения заметки!")
        break
    elif difference_days <= 0:
        print("До истечения срока исполнения осталось", -difference_days, "дней")
        break
    elif difference_days >= 0:
        print("Внимание! Срок исполнения заметки истек ", difference_days, "дней назад")
        break
