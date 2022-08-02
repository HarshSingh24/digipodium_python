def cube(limit):
    for i in range(1,limit+1):
        yield i**3

def fib(limit):
    a,b = 0,1
    for i in range(limit):
        yield a
        a,b = b,a+b

for c in cube(10):
    print(c)

for f in fib(15):
    print(f,end='| ')

# wap to generate a list of even squares using generators
# wap to generate a list of acronyms from a list of words using generators and *args

def even_square(limit):
    for i in range(limit):
        if i%2 == 0:
            yield i**2

for j in even_square(20):
    print(j)

