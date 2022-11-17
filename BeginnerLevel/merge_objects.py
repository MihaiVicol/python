import collections
import unittest


def merge_tuples_lists_integers_strings_floats(x, y):
    """
    merges two lists or tuples or integers or strings or floats
    parameters are the same type
    :param x: lists or tuples or integers or strings or floats
    :param y: lists or tuples or integers or strings or floats
    :return:  merged object of x and y
    """
    return x + y


def merge_sets(x, y):
    """
    merges two sets
    :param x: set
    :param y: set
    :return: merged set of x and y
    """
    return x.union(y)


def merge_dicts(x, y):
    """
    merges two dictionaries
    :param x: dictionary
    :param y: dictionary
    :return: merged dictionary of x and y
    """
    for k, v in y.items():
        if isinstance(v, collections.abc.Mapping):
            x[k] = merge_dicts(x.get(k, {}), v)
        else:
            if k not in x:
                x[k] = v
            elif not isinstance(x[k], type(v)):
                x[k] = x[k], v
            elif isinstance(x[k], (list, float, str, int)):
                x[k] = merge_tuples_lists_integers_strings_floats(x[k], v)
            elif isinstance(x[k], set):
                x[k] = merge_sets(x[k], v)
    return x


def merge(x, y):
    """
    merges any two objects
    :param x: any object
    :param y: any object
    :return: merged object of x and y
    """
    if not isinstance(x, type(y)):
        return x, y
    else:
        if isinstance(x, (list, float, str, int)):
            return merge_tuples_lists_integers_strings_floats(x, y)
        elif isinstance(x, set):
            return merge_sets(x, y)
        elif isinstance(x, dict):
            return merge_dicts(x, y)


class MergeTest(unittest.TestCase):
    def test_merge_dict(self):
        d1 = {'x': [[1, 2, 3]], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
        d2 = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': 'wer', 'd': 123}
        res = merge(d1, d2)
        self.assertEqual(res, {'x': [[1, 2, 3], 4, 5, 6], 'y': 5, 'z': {1, 2, 3, 4}, 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], 'wer'), 'd': 123})

    def test_merge_different_types(self):
        d1 = [1, 2, 3]
        d2 = (1, 2, 3)
        res = merge(d1, d2)
        self.assertEqual(res, ([1, 2, 3], (1, 2, 3)))

    def test_merge_dict_in_depth(self):
        d1 = {'t': {'y': {'z': 12}}}
        d2 = {'t': {'y': {'z': 13}}}
        res = merge(d1, d2)
        self.assertEqual(res, {'t': {'y': {'z': 25}}})

    def test_merge_lists(self):
        d1 = [1, 2, 3]
        d2 = [1, 2, 3]
        res = merge(d1, d2)
        self.assertEqual(res, [1, 2, 3, 1, 2, 3])
