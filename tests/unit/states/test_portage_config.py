"""
:codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from saltext.gentoo.states import portage_config


@pytest.fixture
def configure_loader_modules():
    return {portage_config: {"__opts__": {"test": True}}}


def test_mod_init():
    """
    Test to enforce a nice structure on the configuration files.
    """
    name = "salt"

    mock = MagicMock(side_effect=[True, Exception])
    with patch.dict(portage_config.__salt__, {"portage_config.enforce_nice_config": mock}):
        assert portage_config.mod_init(name)

        assert not portage_config.mod_init(name)


def test_flags():
    """
    Test to enforce the given flags on the given package or ``DEPEND`` atom.
    """
    with patch("traceback.format_exc", MagicMock(return_value="SALTSTACK")):
        name = "salt"

        ret = {"name": name, "result": False, "comment": "SALTSTACK", "changes": {}}

        mock = MagicMock(side_effect=Exception("error"))
        with patch.dict(portage_config.__salt__, {"portage_config.get_missing_flags": mock}):
            assert portage_config.flags(name, use="openssl") == ret

            assert portage_config.flags(name, accept_keywords=True) == ret

            assert portage_config.flags(name, env=True) == ret

            assert portage_config.flags(name, license=True) == ret

            assert portage_config.flags(name, properties=True) == ret

            assert portage_config.flags(name, mask=True) == ret

            assert portage_config.flags(name, unmask=True) == ret

            ret.update({"comment": "", "result": True})
            assert portage_config.flags(name) == ret
