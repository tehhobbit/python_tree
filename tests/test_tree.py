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


def test_filter_always_true():
    tree = Tree()
    node = Node("Test")
    tree.add_node(node)
    node2 = Node("Test2")
    node.add_child(node2)
    data = tree.filter(lambda x: True)
    assert data == [node, node2]


def test_filter_always_false():
    tree = Tree()
    node = Node("Test")
    tree.add_node(node)
    node2 = Node("Test2")
    node.add_child(node2)
    data = tree.filter(lambda x: False)
    assert data == []


def test_filter_match_one_node():
    tree = Tree()
    node = Node("Test")
    tree.add_node(node)
    node2 = Node("Test2")
    tree.add_node(node2, parent=node)
    data = tree.filter(lambda x: x.name == "Test2")
    assert data == [node2]


def test_filter_without_root():
    tree = Tree()
    with pytest.raises(NoRootNode) as e:
        tree.filter(lambda x: True)
    assert e.value.args[0] == "There is no root node"
