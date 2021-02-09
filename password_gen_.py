"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

import random
import string


def main():
    choice = input(
        "Меню: \n"
        "1. Сгенерировать простой пароль.\n"
        "2. Сгенерировать средний пароль.\n"
        "3. Сгенерировать сложный пароль.\n"
        "4. Выход.\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == '1':
        low_pass()
    elif choice == '2':
        med_pass()
    elif choice == '3':
        strong_pass()


def low_pass():
    l_pass_list = random.sample(string.ascii_lowercase, 8)
    print('Ваш пароль:', ''.join(l_pass_list))


def med_pass():
    m_pass_list = random.sample((string.ascii_letters + string.digits), 8)
    print('Ваш пароль:', ''.join(m_pass_list))


def strong_pass():
    p_digit = p_uplet = p_downlet = p_spec = 0
    pass_string = None
    while p_digit == 0 or p_uplet == 0 or p_downlet == 0 or p_spec == 0:
        p_digit = p_uplet = p_downlet = p_spec = 0
        s_pass_length = random.randint(8, 16)
        s_pass_res = random.sample((string.ascii_letters + string.digits + string.punctuation), s_pass_length)
        pass_string = ''.join(s_pass_res)
        for i in pass_string:
            if str.isdigit(i):
                p_digit += 1
            elif str.islower(i):
                p_downlet += 1
            elif str.isupper(i):
                p_uplet += 1
            else:
                p_spec += 1
    print('Ваш пароль:', pass_string)


if __name__ == '__main__':
    main()
