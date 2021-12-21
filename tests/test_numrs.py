import pytest
import numrs as nr


def test_cmp():
    assert nr.Array([1]) == nr.Array([1])
    assert nr.Array([]) == nr.Array([])


def test_init():
    nr.Array([1.0, 2.0, 3.0])
    nr.Array([1, 2, 3])


def test_len():
    assert len(nr.Array([x for x in range(200)])) == 200


def test_get():
    x = nr.Array([6, 2, 5])
    assert x[0] == 6
    assert x[1] == 2
    assert x[2] == 5
    with pytest.raises(IndexError):
        x[3]


def test_set():
    x = nr.Array([6])
    x[0] = 7.0
    assert x[0] == 7.0


def test_add():
    x = nr.Array([1, 2, 3])
    y = nr.Array([1, 1, 1])
    res = nr.Array([2, 3, 4])
    assert x + y == res


def test_sub():
    x = nr.Array([1, 2, 3])
    y = nr.Array([1, 1, 1])
    res = nr.Array([0, 1, 2])
    assert x - y == res


def test_mean():
    assert nr.Array([]).mean() == 0.0
    assert nr.Array([1]).mean() == 1.0
    assert nr.Array([1, 5, 12, 26]).mean() == 11.0


def test_median():
    assert nr.Array([]).median() == 0.0
    assert nr.Array([1]).median() == 1.0
    assert nr.Array([1, 7, 19]).median() == 7.0
    assert nr.Array([1, 5, 12, 26]).median() == 8.5
