def forall(pred, iterable):
    return all(pred(x) for x in iterable)


def exists(pred, iterable):
    return any(pred(x) for x in iterable)


def at_least(n, pred, iterable):
    return sum(1 for x in iterable if pred(x)) >= n


def at_most(n, pred, iterable):
    return sum(1 for x in iterable if pred(x)) <= n

pred = lambda x: x > 3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(forall(pred, list))
print(exists(pred, list))
print(at_least(3, pred, list))
print(at_most(3, pred, list))