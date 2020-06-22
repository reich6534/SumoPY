from nose.tools import *
from bmc.book import Book

def setup():
    print ("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_bookname():
    matthew = Book("Matthew", 27)
    assert_equal(matthew.name, "Matthew")

@raises (IndexError)
def test_small():
    B = Book("Genesis", 50)
    B.set_chapter_descr(0, "This should fail")


@raises(IndexError)
def test_big():
    B = Book("Revelation", 22)
    B.set_chapter_descr(23, "This should fail")

@raises(ValueError)
def test_bigbook():
    Book("Exodus", 151)

@raises(ValueError)
def test_smallbook():
    Book("Obadiah", 0)

