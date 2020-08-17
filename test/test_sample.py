import code.main as cm

def test_correctness():
    assert cm.inc(3) == 4

def test_incorrectness():
    assert not cm.inc(3) == 5