"""
:codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

import saltext.gentoo.states.eselect as eselect


@pytest.fixture
def configure_loader_modules():
    return {eselect: {}}


def test_set_():
    """
    Test to verify that the given module is set to the given target
    """
    name = "myeselect"
    target = "hardened/linux/amd64"

    ret = {"name": name, "result": True, "comment": "", "changes": {}}

    mock = MagicMock(return_value=target)
    with patch.dict(eselect.__salt__, {"eselect.get_current_target": mock}):
        comt = f"Target '{target}' is already set on '{name}' module."
        ret.update({"comment": comt})
        assert eselect.set_(name, target) == ret
