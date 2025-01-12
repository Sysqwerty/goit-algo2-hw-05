from bloom import BloomFilter

# Технічні умови
# 1. Реалізуйте клас BloomFilter, який забезпечує додавання елементів до фільтра та перевірку
# наявності елемента у фільтрі.
# 2. Реалізуйте функцію check_password_uniqueness, яка використовує екземпляр
# BloomFilter та перевіряє список нових паролів на унікальність. Вона має повертати результат перевірки для кожного
# пароля.
# 3. Забезпечте коректну обробку всіх типів даних. Паролі слід обробляти просто як рядки, без хешування.
# Порожні або некоректні значення також мають бути враховані та оброблені належним чином.
# 4. Функція та клас мають працювати з великими наборами даних, використовуючи мінімум пам’яті.


def check_password_uniqueness(
    bloom_filter: BloomFilter, passwords: [str]
) -> (str, str):
    results = {}

    for password in passwords:
        if bloom_filter.contains(password):
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
    return results


if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")
