from types import GeneratorType

def countdown(num: int):
    print("starting")
    while(num > 0):
        yield num
        num -=1

cd = countdown(5)

try:
    while True:
        print(next(cd))
except Exception:
    print('Done')


def fibonacci(limit: int):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(10)

for i in fib:
    print(i)