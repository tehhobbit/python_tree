from unittest.mock import patch
import pytest


@pytest.fixture
def uuid():
    with patch("python_tree.node.uuid") as uuid:
        uuid.uuid4.return_value = "uuid"
        yield uuid
