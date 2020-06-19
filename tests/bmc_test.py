from nose.tools import *
from bmc.book import Book

def setup():
    print ("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_bookname():
    matthew = Book("Matthew", 27)
    assert_equal(matthew.name, "Matthew")

@raises(ValueError)
def test_bigbook():
    Book("Exodus", 151)

@raises(ValueError)
def test_smallbook():
    Book("Obadiah", 0)