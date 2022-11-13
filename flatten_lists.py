import unittest


def flatten(list_to_flatten, depth):
    """
    flatten list to until given depth or maximum possible
    :param list_to_flatten: list
    :param depth: int
    :return: flattened list
    """
    if depth == 0:
        return list_to_flatten
    aux_list = []
    for elem in list_to_flatten:
        if depth > 0 and isinstance(elem, list):
            aux_list.extend(flatten(elem, depth-1))
        else:
            aux_list.append(elem)
    return aux_list


def make_flatten(list_a, list_b, depth):
    """
    flatten two list with flatten function
    :param list_a: list
    :param list_b: list
    :param depth: int
    :return: tuple with list flattened
    """
    return flatten(list_a, depth), flatten(list_b, depth)


class FlattenTest (unittest.TestCase):
    def test_different_depth_elements(self):
        res = make_flatten([[[[[[1, 2, 3]]], 3, 4], 5]], [[[[4, 5, 6]], 7]], 20)
        self.assertEqual(([1, 2, 3, 3, 4, 5], [4, 5, 6, 7]), res, "i'm testing two lists")

    def test_depth_lower(self):
        r = make_flatten([[[[[[1, 2, 3]]], 3, 4], 5]], [[[[4, 5, 6]], 7]], 4)
        self.assertEqual(([[1, 2, 3], 3, 4, 5], [4, 5, 6, 7]), r, "i'm testing two lists")

    def test_empty_list(self):
        res = make_flatten([], [], 20)
        self.assertEqual(res, ([], []))
