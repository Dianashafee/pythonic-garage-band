from pythonic_garage_band import __version__
from pythonic_garage_band.band import *



def test_version():
    assert __version__ == '0.1.0'

# def test_guitarist_str():
#     joan = Guitarist("Joan Jett")
#     actual = str(joan)
#     expected = "Guitarist Joan Jett"
#     assert actual == expected


def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
