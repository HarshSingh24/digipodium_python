num = [200, 500, 900]
out = map(str, num)
print(list(out))


out = map(lambda i : i//10, num)
print(list(out))