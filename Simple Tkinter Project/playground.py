def add(*args):
    sum = 0
    for n in args:
        sum = n + sum
#    print(sum)


add(1,1,1,1,1)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)
