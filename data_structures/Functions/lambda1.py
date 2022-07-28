f = lambda x: x + 3 * 5
g = lambda x,y: x**2 + y**2

print(f(2))
print(g(2,5))
print(g(f(2),f(4)))