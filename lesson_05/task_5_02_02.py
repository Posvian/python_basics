# С ключевым словом yield: Вычислять и
# возвращать само число и накопительную сумму
# этого и предыдущих чисел.

def iterator_with_yield(n):
    num = 1
    num_sum = 0
    while num <= n:
        if num**2 < 200:
            num_sum += num
            yield num, num_sum
        num += 2


gen1 = iterator_with_yield(17)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))