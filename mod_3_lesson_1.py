from function import countdown, greeting, fibonachi, FizzBuzz, some_func

# greeting("Lee", "Djon")
# k = fibonachi(6)
# print("Result:", k)


# FizzBuzz()
#some_func("Hello", 2, 4, "You", 3)

# countdown(10)

# Looking at the below code, write down the final values of A0, A1, ...An.

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
A7 = [i if i % 2 else 0 for i in A1 if 2 < i < 8]

print("A2:", A2)
#print("A1:", A1)
# print
