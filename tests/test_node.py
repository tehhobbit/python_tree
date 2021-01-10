import pytest
from python_tree.node import Node, BaseNode


def test_base_node_cant_be_used():
    with pytest.raises(TypeError):
        BaseNode()


def test_new_node():
    node = Node(name="A node", node_id="derp")
    assert node.name == "A node"
    assert node.node_id == "derp"


def test_node_without_id(uuid):
    node = Node(name="test")
    assert node.node_id == "uuid"
    assert node.name == "test"


def test_node_add_child():
    node = Node(name="test")
    node.add_child(Node("test2"))
    assert node.children
    assert node.children[0].name == "test2"
