import copy
import unittest


def is_hashable(thing):
    """
    check if parameter is an instance of hashable objects
    :param thing: any object
    :return: boolean value that represents if the parameter is hashable
    """
    if isinstance(thing, (int, float, str, tuple, range, frozenset)):
        return True
    return False


def swap_keys_values(dict_to_swap):
    """
    swap keys with values if possible, print a message if is not possible
    :param dict_to_swap: dictionary
    :return: dictionary with swapped keys-values
    """
    copy_dict = {}
    for key in dict_to_swap:
        if is_hashable(dict_to_swap[key]):
            copy_dict[dict_to_swap[key]] = key
        else:
            copy_dict[key] = dict_to_swap[key]
            print('value ' + str(dict_to_swap[key]) + ' cannot be key')
    return copy_dict


class TestHashable(unittest.TestCase):
    def test_hashable_objects(self):
        integer = 23
        floating = float(23)
        string = "str"
        tuple_obj = (1, 2, 3)
        self.assertEqual((is_hashable(integer), is_hashable(floating), is_hashable(string), is_hashable(tuple_obj)),
                         (True, True, True, True))

    def test_non_hashable_objects(self):
        dictionary = {}
        self.assertEqual(is_hashable(dictionary), False)


class TestSwapKeys(unittest.TestCase):
    def test_successful_swap(self):
        a = {'a': 1, 'b': 456}
        res = swap_keys_values(a)
        self.assertDictEqual(res, {1: 'a', 456: 'b'})

    def test_unsuccessful_swap(self):
        b = {'a': [1, 2, 3], 'b': (1, 2, 3)}
        res = swap_keys_values(b)
        self.assertDictEqual(res, {'a': [1, 2, 3], (1, 2, 3): 'b'})



