def add(x, y):
    return x + y


def zip(*iterable):
    n = min([len(i) for i in iterable])
    for i in range(n):
        yield tuple([iterator[i] for iterator in iterable])


def filter(function, iterable):
    if function is None:
        for i in iterable:
            if i:
                yield i
    else:
        for i in iterable:
            if function(i):
                yield i


def enumerate(items, start=0):
    for i in items:
        yield start, i
        start += 1


def map(function, iterable):
    for i in iterable:
        yield function(i)


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def foo(n):
    return n % 2 == 0


def func(x):
    return x * 2


ls1 = [1, 2, 3, 4, 5, 6]
ls2 = ["Roman", 'Alex', 'Georg', 'Arman']
ls3 = ['84', '85', '89', '45']
k = list(zip(ls1, ls2, ls3))
q = list(filter(foo, ls1))
w = list(enumerate(ls2))
p = list(map(func, ls1))
print(q)
print(k)
print(w)
print(p)
s = counter()
print(s())
print(s())
print(s())
