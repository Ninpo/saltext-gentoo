"""
:codeauthor: Ryan Lewis (ryansname@gmail.com)

pytest.unit.modules.portage_flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from saltext.gentoo.modules import portage_config

pytest.importorskip("portage", reason="System is not gentoo/funtoo.")


def setup_loader_modules():
    return {}


def test_get_config_file_wildcards():
    pairs = [
        ("*/*::repo", "/etc/portage/package.mask/repo"),
        ("*/pkg::repo", "/etc/portage/package.mask/pkg"),
        ("cat/*", "/etc/portage/package.mask/cat_"),
        ("cat/pkg", "/etc/portage/package.mask/cat/pkg"),
        ("cat/pkg::repo", "/etc/portage/package.mask/cat/pkg"),
    ]

    for atom, expected in pairs:
        assert portage_config._get_config_file("mask", atom) == expected
