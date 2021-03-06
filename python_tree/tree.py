from __future__ import annotations
import copy
from python_tree.node import Node, BaseNode
from python_tree.exceptions import NoRootNode
from typing import Optional, List, Callable


class Tree:
    """ Represents a tree"""
    def __init__(self, root_node: Optional[Node] = None):
        self.root = root_node
        self.node_ids: List[str] = []

    def add_node(self, node: Node, parent: Optional[Node] = None) -> Node:
        """ Add a node to the tree.

        Args:
            node: Node to be added.
            parent: Parent node to add the node to.

        Returns:
            The node added to the tree.

        Raises:
            NoRootNode if root node is not set and parent is specified.

        """
        if not self.root and parent:
            raise NoRootNode("You need to have a root node")
        elif not self.root and not parent:
            self.root = node
            return node
        elif parent:
            parent.add_child(node)
            return node
        else:
            raise NoRootNode("There is a root node but you have not given a parent for new node")

    def filter(self, fn: Callable) -> List[BaseNode]:
        """ Filter out nodes.

        Args:
            fn: Function to test if a node matches a specific condition.

        Returns:
            List of all nodes where fn returned True

        """
        if not self.root:
            raise NoRootNode("There is no root node")
        return [node for node in self.all_nodes if fn(node)]

    def map(self, fn: Callable) -> Tree:
        """ Apply fn to each node in the tree.

        Args:
            fn: Transformation to apply to each node.

        Returns:
            A tree with all nodes transformed.

        """
        if not self.root:
            raise NoRootNode("There is no root node")
        [fn(node) for node in self.all_nodes]
        return self

    @property
    def all_nodes(self):
        return self._get_all_nodes(self.root)

    def get_node(self, node_id: str) -> Node:
        return next((x for x in self.all_nodes if x.node_id == node_id))

    def subtree(self, node: Node):
        new_root = copy.copy(node)
        return Tree(root_node=new_root)

    def _get_all_nodes(self, root):
        yield root
        for child in root.children:
            yield from self._get_all_nodes(child)
