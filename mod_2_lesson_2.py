x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
try:
    result = x/y
    print("x/y = ", result)
except ZeroDivisionError:
    print("Ділення на 0 забороненно!")
else:
    print("It is ok")
finally:
    print("Finally block")
