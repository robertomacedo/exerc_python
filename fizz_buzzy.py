
for p in range(1, 50):
    if p % 3 == 0 and p % 5 == 0:
        print("FizzBuzz")
    elif p % 3 == 0:
        print("Fizz")
    elif p % 5 == 0:
        print("Buzz")

    else:

        print(p)
