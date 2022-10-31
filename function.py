from re import S


def greeting(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")


def fibonachi(n):
    if n >= 2:
        r = fibonachi(n-1) + fibonachi(n-2)
        return r
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return "Error number"


def FizzBuzz():
    """Задача FizzBuzz 

    Выведите каждое число от 1 до 100 (оба включены) на новой строке. 
    Числа, которые кратны 3, печатают “Fizz” вместо числа. Для чисел, 
    которые кратны 5, выведите “Buzz” вместо числа. Для числа, кратного 
    как 3, так и 5, выведите “FizzBuzz” вместо чисел."""

    for num in range(1, 101):
        if num % 15:
            print("FizzBuzz")
        elif num % 3:
            print("Fizz")
        elif num % 5:
            print("Buzz")
        else:
            print(num)


def some_func(*args):
    for arg in args:
        print(arg)


def dist_func(**kwargs):
    for key, value in kwargs.items():
        print("Key:", key, "Value:", value)


def factorial(k):
    if k == 1:
        return 1
    else:
        return k*factorial(k-1)


def countdown(n):
    print(f"Countdown {n}:")
    if n == 0:
        return
    else:
        countdown(n-1)


if __name__ == '__main__':
    print("You imported function.py")
    greeting("Djon", "Veek")
