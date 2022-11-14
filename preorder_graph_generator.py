
def preorder_generator(graph_tuple):
    for i in graph_tuple:
        if isinstance(i, tuple):
            yield from preorder_generator(i)
        elif i:
            yield i


graph_t = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
for node in preorder_generator(graph_t):
    print(node)
