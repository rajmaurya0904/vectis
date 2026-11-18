"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import vectis


def test_version_is_set() -> None:
    assert vectis.__version__
