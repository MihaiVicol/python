def read_from_file():
    file = open("dictionaries", "r")
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
    f = open('sorted_dictionaries', 'w')
    list_original = read_from_file()
    for i in list_dict:
        f.write(str(list_original.index(i)) + '\n')
    f.close()


def cmp_func(b):
    sat = sorted(b)
    return int(b[sat[0]])


def sort(list_to_sort):
    list_to_sort.sort(key=cmp_func)
    return list_to_sort


list_from_file = read_from_file()
print(sort(list_from_file))
write(list_from_file)




