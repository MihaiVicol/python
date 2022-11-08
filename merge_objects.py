a = {'x': [[1, 2, 3]], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': 'wer', 'd': 123}


def merge(x, y, z={}):
    if type(x) is type(y):
        for items_x, items_y in zip(x, y):
            if type(x[items_x]) is type(y[items_y]):
                if isinstance(x[items_x], (int, float, str, list)):
                    z[items_x] = x[items_x]
                    z[items_x] += y[items_y]
                elif isinstance(x[items_x], set):
                    z[items_x] = x[items_x]
                    z[items_x].update(y[items_y])
                elif isinstance(x[items_x], dict):
                    merge(x[items_x], y[items_y])
            else:
                z[items_x] = (x[items_x], y[items_y])
        if len(y) > len(x):
            tuple_y = tuple(y.items())
            for k in range(len(x), len(y)):
                z[tuple_y[k][0]] = tuple_y[k][1]
        return z
    else:
        return x, y


print(merge(a, b))
