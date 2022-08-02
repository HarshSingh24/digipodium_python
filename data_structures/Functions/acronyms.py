# wap to generate a list of acronyms from a list of words using generators and *args


def acronyms(*limit):
    for word in limit:
        yield "".join([i[0].upper() for i in word.split()])

for j in acronyms('project manager', 'data analyst', 'data scientist'):
    print(j)