# Написать генератор нечётных чисел от 1 до n
# (включительно), используя ключевое слово yield.
# Полностью истощить генератор.

def iterator_with_yield(n):
    num = 1
    while num <= n:
        yield num
        num += 2


gen1 = iterator_with_yield(14)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))