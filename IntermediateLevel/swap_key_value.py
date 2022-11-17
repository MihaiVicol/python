
def is_hashable(thing):
    try:
        hash(thing)
    except TypeError:
        return False
    else:
        return True


a = {'a': 1, 'b': 456}
b = {'a': [1, 2, 3], 'b': (1, 2, 3)}


def swap_keys_values(dict_to_swap):
    copy_dict = dict_to_swap.copy()
    for key in copy_dict:
        if is_hashable(copy_dict[key]):
            dict_to_swap[dict_to_swap[key]] = key
            dict_to_swap.pop(key)
        else:
            print('value ' + str(copy_dict[key]) + ' cannot be key')
    return dict_to_swap


print(swap_keys_values(b))
