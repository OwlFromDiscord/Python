import datetime, birthday_messages

today = datetime.date.today()
next_birthday = datetime.date(2024, 12, 10)
days_away = next_birthday - today

if next_birthday == today:
    print(birthday_messages.random_message)
else:
    print("My birthday is " + str(days_away) + " away!")