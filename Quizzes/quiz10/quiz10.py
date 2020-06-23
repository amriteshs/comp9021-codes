# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


import sys
from random import seed, choice
from quiz10_binary_tree_adt import *
from collections import deque


def print_growing_up(tree):
    height = tree.height()
    q = deque([tree.left_node, tree.right_node])
    t = list([(' ' * ((2 ** height) - 1)) + str(tree.value)])

    for level in range(height - 1, -1, -1):
        flag = False
        level_str = str()

        for i in range(len(q)):
            if not flag:
                level_str = ' ' * ((2 ** level) - 1)
                flag = True
            else:
                level_str += (' ' * ((2 ** (level + 1)) - 1))

            if q[i] is None or q[i].value is None:
                level_str += ' '
            else:
                level_str += str(q[i].value)

        t.append(level_str)

        q_len = len(q)
        while q_len:
            if q[0] is None:
                q.append(None)
                q.append(None)
            else:
                q.append(q[0].left_node)
                q.append(q[0].right_node)

            q.popleft()
            q_len -= 1

    for i in range(len(t) - 1, -1, -1):
        t[i] = t[i].rstrip()
        print(t[i])


try:
    seed_arg, nb_of_nodes = (int(x) for x in
                             input('Enter two integers, with the second one between 0 and 10: '
                                   ).split()
                             )
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_growing_up(tree)
