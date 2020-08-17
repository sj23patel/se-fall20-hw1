import sys
sys.path.append("../")
import script

def test_should_pass():
    assert code.inc(3) == 4

def test_should_fail():
    assert not code.inc(3) == 5