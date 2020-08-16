import code

def test_should_pass():
    assert code.inc(3) == 4

def test_should_fail():
    assert code.inc(3) == 5