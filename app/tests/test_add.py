from app.main import add


def test_add():
    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add(-3, 3) == 0
