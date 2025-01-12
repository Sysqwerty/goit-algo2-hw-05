import json
import timeit

from datasketch import HyperLogLog

# Технічні умови
# 1. Завантажте набір даних із реального лог-файлу lms-stage-access.log, що містить інформацію про IP-адреси.
# 2. Реалізуйте метод для точного підрахунку унікальних IP-адрес за допомогою структури set.
# 3. Реалізуйте метод для наближеного підрахунку унікальних IP-адрес за допомогою HyperLogLog.
# 4. Проведіть порівняння методів за часом виконання.


def upload_data(path: str) -> list:
    data: list = []

    with open(path, "r", encoding="UTF-8") as f:
        for line in f:
            if line == "\n" or line == "" or (not json.loads(line)["remote_addr"]):
                continue
            data.append(json.loads(line))

    return data


def count_unique_ip_set(data: list):
    my_set = set()

    for item in data:
        my_set.add(item["remote_addr"])
    return len(my_set)


def count_unique_ip_hll(data: list):
    hll = HyperLogLog(p=10)

    for item in data:
        hll.update(item["remote_addr"].encode("utf-8"))
    return hll.count()


def compare_unique_ip():
    data = upload_data("lms-stage-access.log")

    # Точний підрахунок
    exact_count = count_unique_ip_set(data)
    exact_time = timeit.timeit(lambda: count_unique_ip_set(data), number=100)

    # Підрахунок HyperLogLog
    hll_count = count_unique_ip_hll(data)
    hll_time = timeit.timeit(lambda: count_unique_ip_hll(data), number=100)

    # Форматований вивід результатів
    print("Результати порівняння:")
    print(f"{'':<20} | {'Точний підрахунок':<20} | {'HyperLogLog':<20}")
    print(f"{'-'*70}")
    print(f"{'Унікальні елементи':<20} | {exact_count:<20} | {hll_count:<20}")
    print(f"{'Час виконання (сек.)':<20} | {exact_time:<20.2f} | {hll_time:<20.2f}")


if __name__ == "__main__":
    compare_unique_ip()
