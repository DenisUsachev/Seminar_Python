fib = lambda N: N if N in (0,1) else fib(N - 1) + (N - 2)
# Если N в диапазоне от (0, 1), то возвращаем N(ставиться до условия), иначе вернём fib(N - 1) + (N - 2)

print(fib(7))