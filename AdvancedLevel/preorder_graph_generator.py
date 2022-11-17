import unittest


def preorder_generator(graph_tuple):
    for i in graph_tuple:
        if isinstance(i, tuple):
            yield from preorder_generator(i)
        elif i:
            yield i


class TestGenerator(unittest.TestCase):
    def test_preorder(self):
        graph_t = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
        res = [node for node in preorder_generator(graph_t)]
        self.assertListEqual(res, ['b', 'a', 'z', 'c', 'zz'])

