import datetime, birthday_messages

today = datetime.today()
next_birthday = datetime.date(2001, 12, 10)
days_away = next_birthday - today

if next_birthday == today:
    print(birthday_messages.random_message)
else:
    print("My birthday is " + days_away + " days away!")