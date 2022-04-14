from math import log2
from graphviz import Digraph
import queue

feature_set = [0, 1, 2]

example_set = [
    ((False, False, False), False),
    ((False, False, True), False),
    ((False, True, False), True),
    ((False, True, True), False),
    ((True, False, False), False),
    ((True, False, True), False),
    ((True, True, False), True),
    ((True, True, True), True),
]


class Node:
    def __init__(self, value):
        self.left = None
        self.left_label = True
        self.value = value
        self.right = None
        self.right_label = False


def count_pos(example_set) -> int:
    classifications = [example[1] for example in example_set]
    return classifications.count(True)


def count_neg(example_set) -> int:
    classifications = [example[1] for example in example_set]
    return classifications.count(False)


def partition_example_set(feature, example_set) -> tuple:
    list_true = list()
    list_false = list()
    for example in example_set:
        if example[0][feature]:
            list_true.append(example)
        else:
            list_false.append(example)
    return (list_true, list_false)


def entropy(example_set) -> float:
    pos = count_pos(example_set)
    neg = count_neg(example_set)
    assert pos + neg == len(example_set)
    pos_frac = pos / float(pos + neg)
    neg_frac = 1 - pos_frac
    if pos_frac == 0:
        return -neg_frac * log2(neg_frac)
    if neg_frac == 0:
        return -pos_frac * log2(pos_frac)
    result = -(pos_frac * log2(pos_frac) + neg_frac * log2(neg_frac))
    assert 0 <= result and result <= 1
    return result


def remainder(feature, example_set) -> float:
    (list_true, list_false) = partition_example_set(feature, example_set)
    true_frac = len(list_true) / float(len(example_set))
    false_frac = 1 - true_frac
    result = true_frac * entropy(list_true) + false_frac * entropy(list_false)
    return result


def gain(feature, example_set) -> float:
    result = entropy(example_set) - remainder(feature, example_set)
    return result


def decision_tree(feature_set, example_set) -> Node:
    if len(example_set) == 0:
        return Node(False)  # arbitrary value

    if count_pos(example_set) == len(example_set):
        return Node(True)
    if count_neg(example_set) == len(example_set):
        return Node(False)

    gains = [(feature, gain(feature, example_set)) for feature in feature_set]
    gains.sort(key=lambda x: x[1], reverse=True)
    max_gain = gains[0]
    partition_feature = max_gain[0]
    (true_frac, false_frac) = partition_example_set(
        partition_feature, example_set)
    new_feature_set = list(feature_set)
    new_feature_set.remove(partition_feature)

    print(f'Feature Set: {list(map(lambda feature: f"X_{feature+1}", feature_set))}')
    print(f'Gains for each feature {gains}')
    print(f'Splitting using feature X_{partition_feature + 1}')

    node = Node(f'X_{partition_feature + 1}')
    node.left = decision_tree(new_feature_set, true_frac)
    node.left_label = True
    node.right = decision_tree(new_feature_set, false_frac)
    node.right_label = False

    return node


def draw_decision_tree(tree):
    dot = Digraph('Decision-Tree')
    q = queue.Queue()
    q.put(('root', tree))
    while not q.empty():
        (node_name, node) = q.get()
        dot.node(name=node_name, label=str(node.value))
        if node.left:
            child_name = node_name+str(node.value) + \
                str(node.left_label)+str(node.left.value)
            dot.node(name=child_name, label=str(node.left.value))
            dot.edge(node_name, child_name, label=str(node.left_label))
            q.put((child_name, node.left))

        if node.right:
            child_name = node_name + \
                str(node.value)+str(node.right_label)+str(node.right.value)
            dot.node(name=child_name, label=str(node.right.value))
            dot.edge(node_name, child_name, label=str(node.right_label))
            q.put((child_name, node.right))
    dot.render()


if __name__ == '__main__':
    tree = decision_tree(feature_set, example_set)
    draw_decision_tree(tree)
