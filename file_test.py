"""Tiny unit tests just to demo GitHub Actions with pytest."""


def test_calc_addition():
    assert 2 + 4 == 6


def test_calc_subtraction():
    """Check subtraction 2 - 4."""
    assert 2 - 4 == -2


def test_calc_multiply():
    """Check multiplication 2 * 4."""
    assert 2 * 4 == 8


def test_hello():
    """Return value equals 'hello'."""
    output = "hello"
    assert output == "hello"
