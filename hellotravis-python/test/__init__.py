import unittest


def get_tests():
    return full_suite()


def full_suite():
    from .utils import UtilsTestCase

    utilssuite = unittest.TestLoader().loadTestsFromTestCase(UtilsTestCase)

    return unittest.TestSuite([utilssuite])
