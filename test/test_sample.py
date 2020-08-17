import code.main as m

def test_should_pass():
    assert m.inc(3) == 4

def test_should_fail():
    assert not m.inc(3) == 5
