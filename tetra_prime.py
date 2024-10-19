import time

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_tetrahedral_numbers(limit):
    """Генерирует тетраэдральные числа до указанного предела."""
    tetrahedral_numbers = []
    k = 1
    while True:
        tetrahedral_num = k * (k + 1) * (k + 2) // 6
        if tetrahedral_num > limit:
            break
        tetrahedral_numbers.append(tetrahedral_num)
        k += 1
    return tetrahedral_numbers

def check_tetrahedral_symmetry(n, existing_numbers, tetrahedral_numbers):
    """
    Проверяет, нарушает ли число тетраэдральную симметрию.
    Представляет число как шар, добавленный к тетраэдру.
    """
    if n == 5:
        return True  # Четвёртый шар соответствует первому простому числу

    # Проверяем остальные числа, добавляемые в структуру
    for num in existing_numbers:
        if abs(num - n) not in tetrahedral_numbers:
            return True  # Нарушение симметрии, число особенное (может быть простым)
    return False  # Симметрия не нарушена

def find_symmetric_primes(limit):
    """Ищет простые числа, которые нарушают тетраэдральную симметрию."""
    primes = []
    symmetric_primes = []

    # Генерируем тетраэдральные числа до указанного лимита
    tetrahedral_numbers = generate_tetrahedral_numbers(limit)

    # Находим все простые числа
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    
    # Проверяем симметрию для каждого простого числа только по тетраэдрическому принципу
    for prime in primes:
        if check_tetrahedral_symmetry(prime, symmetric_primes, tetrahedral_numbers):  
            symmetric_primes.append(prime)

    return symmetric_primes

def main():
    # Начало замера времени
    start_time = time.time()

    limit = int(input("Введите предел для поиска простых чисел: "))
    symmetric_primes = find_symmetric_primes(limit)
    
    # Конец замера времени
    end_time = time.time()
    elapsed_time = end_time - start_time  # Время выполнения

    # Выводим только последние 20 простых чисел
    print(f"Простые числа, нарушающие тетраэдральную симметрию до {limit}: {symmetric_primes[-20:]}")
    print(f"Всего найдено простых чисел с нарушенной симметрией: {len(symmetric_primes)}")
    print(f"Время расчета: {elapsed_time:.2f} секунд")

if __name__ == "__main__":
    main()
