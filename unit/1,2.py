def is_palindrome(data):
    return data == data[::-1]

def run_tests():
    test_cases = [
        ("radar", True),
        ("level", True),
        ("hello", False),
        ("noon", False),
        ("madam", True),
        ("python", False)
    ]

    for data, expected_result in test_cases:
        result = is_palindrome(data)
        if result == expected_result:
            print("YES")
        else:
            print("NO")
            return

def main():
    choice = input("Введите '1' для тестирования функции или '2' для ввода строки и проверки на палиндром: ")
    if choice == '1':
        run_tests()
    elif choice == '2':
        input_string = input("Введите строку: ")
        if is_palindrome(input_string):
            print("YES")
        else:
            print("NO")
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    main()
