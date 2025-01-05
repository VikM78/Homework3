def check_email(email_address=''):
    email_symbol = '@'
    check_list = ('.com', '.ru', '.net')
    check_email = False
    if email_symbol in email_address:
        if email_address.lower().endswith(check_list):
            check_email = True
    return check_email

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    send_email = True
    if not (check_email(recipient) and check_email(sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        send_email = False
        return send_email
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        send_email = False
        return send_email
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!\nПисьмо успешно отправлено с адреса {sender} на адрес {recipient}")
    print()

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')