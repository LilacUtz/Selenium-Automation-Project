import unittest
from MainPageTitlesTests import MainPageTitlesTests
from OuterLinksTests import OuterLinksTests
from MainPageBoxTests import MainPageBoxTests


def suite():
    loader = unittest.TestLoader()
    my_suit = unittest.TestSuite()
    my_suit.addTest(loader.loadTestsFromTestCase(MainPageTitlesTests))
    print("MainPageTitlesTests - FINISHED")
    my_suit.addTest(loader.loadTestsFromTestCase(MainPageBoxTests))
    print("MainPageBoxTests - FINISHED")
    my_suit.addTest(loader.loadTestsFromTestCase(OuterLinksTests))
    print("OuterLinksTests - FINISHED")

    return my_suit


runner = unittest.TextTestRunner()
runner.run(suite())

