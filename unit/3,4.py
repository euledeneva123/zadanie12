import re

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+7|8)(\s*)?(\()?\d{3}(\))?(\s*|-)?\d{3}(\s*|-)?\d{2}(\s*|-)?\d{2}$'
    return re.match(pattern, number) is not None

def run_tests():
    test_cases = [
        ("+79991234567", True),
        ("8(999)1234567", True),
        ("+7 999 123-45-67", True),
        ("89991234567", True),
        ("+7(999)123-45-67", True),
        ("8999 123 45 67", True),
        ("8999-123-45-67", True),
        ("899912345", False),
        ("+1234567890", False),
        ("+799912345678", False),
        ("1234567890", False),
        ("+999(123)4567890", False),
        ("+7999123456a", False)
    ]

    all_passed = True

    for number, expected_result in test_cases:
        result = is_correct_mobile_phone_number_ru(number)
        if result == expected_result:
            print("YES")
        else:
            print("NO")
            all_passed = False

    if all_passed:
        print("Все тесты пройдены успешно.")
    else:
        print("Не все тесты пройдены.")

def main():
    choice = input("Введите '1' для тестирования функции или '2' для ввода номера и проверки на корректность: ")
    if choice == '1':
        run_tests()
    elif choice == '2':
        input_number = input("Введите номер мобильного телефона: ")
        if is_correct_mobile_phone_number_ru(input_number):
            print("YES")
        else:
            print("NO")
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    main()
