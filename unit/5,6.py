import re

def strip_punctuation_ru(data):
    return re.sub(r'[^\w\s]', '', data)

def run_tests():
    test_cases = [
        ("Это, текст. С знаками! Препинания?", "Это текст С знаками Препинания"),
        ("Тестовая-строка с знаками.", "Тестоваястрока с знаками")
    ]

    all_passed = True

    for data, expected_result in test_cases:
        result = strip_punctuation_ru(data)
        if result == expected_result:
            print("YES")
        else:
            print("NO")
            all_passed = False

    if all_passed:
        print("Все тесты пройдены успешно.")
    else:
        print("Не все тесты пройдены.")

    input_text = input("Введите текст с знаками препинания: ")
    result = strip_punctuation_ru(input_text)
    print(result)

if __name__ == "__main__":
    run_tests()
