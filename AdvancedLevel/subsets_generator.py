def subsets_generator(set_to_subset):
    for i in range(1 << len(set_to_subset)):
        t = []
        for j in range(len(set_to_subset)):
            if (i & (1 << j)) > 0:
                t.append(list(set_to_subset)[j])
        yield t


s = set([1, 2, 3])
for p in subsets_generator(s):
    print(p)
