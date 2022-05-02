# С ключевым словом yield - как в задании 1:
# генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.

def iterator_with_yield(n):
    num = 1
    while num <= n:
        if num**2 < 200:
            yield num
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