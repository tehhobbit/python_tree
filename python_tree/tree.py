from python_tree.node import Node, BaseNode
from python_tree.exceptions import NoRootNode
from typing import Optional, List, Callable


class Tree:
    """ Represents a tree"""
    def __init__(self):
        self.root = None

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
        return self._filter_nodes(fn=fn, root_node=self.root, nodes=[])

    def _filter_nodes(self, fn: Callable, root_node: BaseNode, nodes: List[BaseNode]) -> List[BaseNode]:
        if fn(root_node):
            nodes.append(root_node)
        for child in root_node.children:
            nodes = self._filter_nodes(fn=fn, root_node=child, nodes=nodes)
        return nodes
