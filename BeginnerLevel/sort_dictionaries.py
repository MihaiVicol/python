import unittest


def read_from_file():
    """
    read a file that contains a list of dictionaries
    keys and values are separated by a whitespace
    dictionaries are separated by new line
    :return: list of dictionaries
    """
    file = open("../venv/dictionaries", "r")
    list_dict_file = []

    for line in file.readlines():
        words_list = line.split()
        a = {}
        for words in range(0, len(words_list)-1, 2):
            a[words_list[words]] = words_list[words+1]
        list_dict_file.append(a)

    file.close()
    return list_dict_file


def write(list_dict):
    """
    write in file indexes of sorted dictionaries
    read again from file to see the indexes of dictionaries
    :param list_dict: list of dictionaries
    :return: None
    """
    f = open('../venv/sorted_dictionaries', 'w')
    list_original = read_from_file()
    for i in list_dict:
        f.write(str(list_original.index(i)) + '\n')
    f.close()


def cmp_func(b):
    """
    compare key, it compares the values of the lowest alphabetical key
    :param b: dictionary
    :return: value of lowest alphabetical key
    """
    sat = sorted(b)
    return int(b[sat[0]])


def sort(list_to_sort):
    """
    sort list of dictionaries
    :param list_to_sort: list of dictionaries
    :return: sorted list
    """
    list_to_sort.sort(key=cmp_func)
    return list_to_sort


list_from_file = read_from_file()
write(list_from_file)


class SortTest(unittest.TestCase):
    def test_sort(self):
        list_ex = read_from_file()
        res = sort(list_ex)
        self.assertEqual(res, [{'ag': '8', 'bd': '23', 'df': '34'}, {'ah': '9', 'bf': '23', 'jd': '34'}, {'aa': '12', 'ba': '33', 'cb': '45'}, {'ac': '11', 'ab': '23', 'cb': '34'}])

    def test_read_file(self):
        res = read_from_file()
        self.assertEqual(res, [{'ac': '11', 'ab': '23', 'cb': '34'},
                               {'ah': '9', 'bf': '23', 'jd': '34'},
                               {'ag': '8', 'bd': '23', 'df': '34'},
                               {'aa': '12', 'ba': '33', 'cb': '45'}])


