""" Module to deal with nodes in the tree """
from __future__ import annotations
from typing import Optional, List, Any
import abc
import uuid


class BaseNode(abc.ABC):

    def __init__(self, name: str, node_id: str, data: Any, parent: Optional[BaseNode] = None) -> None:
        self.node_id = node_id
        self.name = name
        self.data = data
        self.parent = parent
        self.children: List[BaseNode] = []

    @abc.abstractmethod
    def add_child(self, child: BaseNode) -> None:
        """ Add a child to the current node
        """


class Node(BaseNode):
    """ Represents a node in a tree.

    Args:
        name: Name of the node
        node_id: Id of the node, if not provided a uuid will be generated
        data: Optional data attached to the node.
        parent: Parent node.

    """
    def __init__(
        self, name: str, node_id: Optional[str] = None, data: Optional[Any] = None, parent: Optional[Node] = None
    ) -> None:
        if not node_id:
            node_id = str(uuid.uuid4())
        super().__init__(name, node_id, data, parent)

    def add_child(self, node: BaseNode) -> None:
        """ Adds a child node

        Args:
            node: Node to be added as a child node
        """
        self.children.append(node)
