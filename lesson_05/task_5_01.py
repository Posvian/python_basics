def iteratir_without_yield(n):
    nums_gen = (num for num in range(1, n+1, 2))
    return nums_gen


gen1 = iteratir_without_yield(11)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
