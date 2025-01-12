from bloom import BloomFilter


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