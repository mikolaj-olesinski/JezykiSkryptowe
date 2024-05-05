import time
from functools import lru_cache

def make_generator(function):
    num = 1
    def help_func():
        nonlocal num
        while True:
            num += 1
            yield function(num - 1)

    return help_func


def make_generator_mem(function):
    @lru_cache
    def memoized_f(i):
        return function(i)

    globals()[function.__name__] = memoized_f
    return make_generator(memoized_f)


def fibbonaci(n):
    if n <= 1:
        return n

    return fibbonaci(n - 1) + fibbonaci(n - 2)


arth_seq = lambda n: n + 2
geo_seq = lambda n: n * 2

def zad4():
    fib_generator = make_generator(fibbonaci)()

    for i in range(10):
        print(f'Fibonacci {i+1}: {next(fib_generator)}')


    
    arth_generator = make_generator(arth_seq)()
    for i in range(5):
        print(f'Arithmetic {i+1}: {next(arth_generator)}')

    geo_generator = make_generator(geo_seq)()
    for i in range(5):
        print(f'Geometric {i+1}: {next(geo_generator)}')

    print(f'Arithmetic {i+1}: {next(arth_generator)}')




def zad5():

    # Bez memoizacji
    s_time_no_memoization = time.time()
    fibonacci_gen_no_memoization = make_generator(fibbonaci)()
    for i in range(30):
        next(fibonacci_gen_no_memoization)
    e_time_no_memoization = time.time()
    elapsed_no_memoization = e_time_no_memoization - s_time_no_memoization

    # Z memoizacją
    s_time_with_memoization = time.time()
    fibonacci_gen_with_memoization = make_generator_mem(fibbonaci)()
    for i in range(30):
        next(fibonacci_gen_with_memoization)
    e_time_with_memoization = time.time()
    elapsed_with_memoization = e_time_with_memoization - s_time_with_memoization

    print(f'Without memoization: {elapsed_no_memoization:.2} seconds')
    print(f'With memoization: {elapsed_with_memoization:.2} seconds')

    fibonnaci_gen = make_generator_mem(fibbonaci)()
    for i in range(10):
        print(f'Fibonacci {i+1}: {next(fibonnaci_gen)}')

if __name__ == "__main__":
    zad5()