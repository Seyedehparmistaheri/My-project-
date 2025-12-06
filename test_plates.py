from plates import is_valid

def test_len():
    assert is_valid("HELLO") == True
    assert is_valid("POIUNKO9") ==  False

def test_aval():
    assert is_valid('22') == False
    assert is_valid("23KJNK") == False
    assert is_valid("K25LP") == False
    assert is_valid("KJM29") == True


def test_pun():
    assert is_valid("GJ,@ML") == False
    assert is_valid("KMC23") == True
    assert is_valid("@mkjl") == False

def test_ja():
     assert is_valid("LM25M") == False
     assert is_valid("Cs05") == False
def test_zero():
    assert is_valid("hn 25l") == False
    assert is_valid("jk-25m") == False
