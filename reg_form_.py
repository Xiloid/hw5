"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
    Программа выводит сообщение:
    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)
"""


def main():
    phone_result = phone()
    email_result = email()
    eqality = pswd()
    asterisks = len(pswd_eqal(eqality))
    pass_result = ''.ljust(asterisks, '*')
    print()
    print(
        'Поздравляем с успешной регистрацией!\n'
        f'Ваш номер телефона: {phone_result}\n'
        f'Ваш email: {email_result}\n'
        f'Ваш пароль: {pass_result}\n'
        )


def phone():
    while True:
        phone_input = input('Введите номер телефона: ')
        digits = ''
        for char in phone_input:
            if char.isdigit():
                digits += char
        if len(digits) >= 9:
            phone_input = '380' + digits[-9:]
        else:
            print('Неверный формат номера!')
            continue
        print('Телефон записан.')
        return phone_input


def email():
    mail_length = ampersand = 0
    mail_input = None
    while mail_length < 6 or ampersand != 1:
        mail_input = input('Введите электропочту: ')
        mail_length = len(mail_input)
        ampersand = mail_input.count('@')
        if mail_length < 6 or ampersand != 1:
            print('Неверный формат почты! Необходимо 6 символов и @')
    print('Email записан.')
    return mail_input


def pswd():
    p_length = p_space = p_upper = p_lower = p_digit = 0
    pswd_input = None
    while p_length < 8 or p_space != 0 or p_upper < 1 or p_lower < 1 or p_digit < 1:
        pswd_input = input('Введите пароль: ')
        p_length = len(pswd_input)
        for i in pswd_input:
            if str.isdigit(i):
                p_digit += 1
            elif str.islower(i):
                p_lower += 1
            elif str.isupper(i):
                p_upper += 1
            elif str.isspace(i):
                p_space += 1
    return pswd_input


def pswd_eqal(eqality):
    ok_pass = input('Подтвердите пароль: ')
    if ok_pass == eqality:
        return ok_pass
    else:
        pswd()


if __name__ == '__main__':
    main()
