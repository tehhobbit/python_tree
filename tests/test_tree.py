import pytest

from python_tree.tree import Tree
from python_tree.node import Node
from python_tree.exceptions import NoRootNode


def test_tree_with_single_root():
    tree = Tree()
    node = Node("test")
    tree.add_node(node)
    assert tree.root == node


def test_no_root_with_parent_set():
    tree = Tree()
    node = Node("test")
    with pytest.raises(NoRootNode) as e:
        tree.add_node(node, parent=node)
    assert e.value.args[0] == "You need to have a root node"


def test_root_node_set_but_no_parent():
    tree = Tree()
    node = Node("Test")
    with pytest.raises(NoRootNode) as e:
        tree.add_node(node)
        tree.add_node(node)
    assert e.value.args[0] == "There is a root node but you have not given a parent for new node"


@pytest.mark.parametrize("fn,result", [
    (lambda x: True, 2),
    (lambda x: False, 0),
    (lambda x: x.name == "Test", 1),
])
def test_filter(fn, result):
    node = Node("Test")
    node2 = Node("Test2")
    result_data = [node, node2]
    tree = Tree()
    tree.add_node(node)
    node.add_child(node2)
    data = tree.filter(fn)
    assert len(data) == result
    assert data == result_data[:result]


def test_filter_without_root():
    tree = Tree()
    with pytest.raises(NoRootNode) as e:
        tree.filter(lambda x: True)
    assert e.value.args[0] == "There is no root node"


def test_map():
    tree = Tree()
    node = Node("Test")
    tree.add_node(node)
    node2 = Node("Test2")
    tree.add_node(node2, parent=node)

    def mapper(node: Node) -> None:
        node.data = 2
    tree = tree.map(mapper)
    for node in tree.all_nodes:
        assert node.data == 2
