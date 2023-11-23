import random
import time


def measure_time(func):
    def wrapper(*args, **kwargs):  # przyjmuje wszystkie możliwe kombinacje argumntów
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sekundy")
        return result

    return wrapper


def monte_carlo_pi(n):
    points_inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1

    return 4 * (points_inside_circle / n)


@measure_time
def my_function():
    time.sleep(1)

@measure_time
def pi_run():
    return monte_carlo_pi(30_000_000)


# my_function()
# for i in range(9):
#     my_function()


# pi = monte_carlo_pi(3_000_000)
# print(pi)

print(pi_run())