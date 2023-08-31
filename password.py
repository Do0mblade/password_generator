import secrets

def create_new(length, characters):
    # создание пароля
    if characters != '':
        return ''.join(secrets.choice(characters) for i in range(length))
    else:
        return 'Выберите символы для пароля'