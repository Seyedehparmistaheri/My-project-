from twttr import shorten

def test_hello():
    assert shorten("hello") == "hll"
    assert shorten("i am parmiss") == " m prmss"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello") == "Hll"
    assert shorten("hello6") == "hll6"
    assert shorten("hel,lo") == "hl,l"



