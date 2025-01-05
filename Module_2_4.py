#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = list(range(100))
numbers.remove(0)
print(numbers)
primes = []
not_primes = []
is_prime = True
len_numbers = len(numbers)
for i in range(len_numbers):
    current_value = numbers[i]
    if current_value > 1:
        for j in range(i):
            if j > 0:
                is_prime = True
                div_value = current_value % numbers[j]
                if div_value == 0:
                    print(f"i={i}, j={j}, {current_value}%{numbers[j]}={div_value}")
                    is_prime = False
                    break
        if is_prime:
            primes.append(current_value)
        else:
            not_primes.append(current_value)
print(f"Primes:     {primes}")
print(f"Not Primes: {not_primes}")
