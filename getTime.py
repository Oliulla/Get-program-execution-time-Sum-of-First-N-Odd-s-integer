# Get program's execution times & sum of first N Integers
"""import time


def myFunction():
    start_time = time.time()

    k = 0
    for i in range(1, n + 1):
        k += i

    end_time = time.time()
    return k, end_time-start_time


n = 10
print(myFunction())"""


# Get program's execution times & sum of first N odd Integers by ranging numbers
import time

print("First N odd's Integer summation")

try:
    def myFunction():
        start_time = time.time()
        j = []
        for k in range(1, n+1):
            if k % 2 == 0:
                continue
            j.append(k)
        summation = (len(j) ** 2)
        print(f"Summation of 1 to {n} is: {summation}")
        end_time = time.time()
        return end_time - start_time


    n = int(input("Enter your number range: "))
    print(f"Program execution time is: {myFunction()}")
except ValueError:
    print("""Sorry, Invalid Value.
please try again with valid value...
Thank you.""")
