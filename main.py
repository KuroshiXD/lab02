def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Создаем список, где True означает, что число простое
    primes[0], primes[1] = False, False  # 0 и 1 не являются простыми

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            # Обнуляем кратные p начиная с p^2
            for i in range(p * p, n + 1, p):
                primes[i] = False

    # Возвращаем список простых чисел
    return [p for p in range(n + 1) if primes[p]]

# Пример использования
n = 50
print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")
