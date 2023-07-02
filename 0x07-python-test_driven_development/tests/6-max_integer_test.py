#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Testing Son!!
    """

    def test_max_integer_no_argrument(self):
        """Test if nothing is given"""
        result = max_integer()
        self.assertIsNone(result)

    def test_max_integer_empty_list(self):
        """Test if nothing is given"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_one_element_list(self):
        """Test if nothing is given"""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_max_integer_all_two_elements(self):
        """Test if nothing is given"""
        result = max_integer([2,3])
        self.assertEqual(result, 3)

    def test_max_integer_all_the_same_elements(self):
        """Test if nothing is given"""
        result = max_integer([2,2,2,2])
        self.assertEqual(result, 2)

    def test_max_integer_all_example_one(self):
        """Test if nothing is given"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_all_example_two(self):
        """Test if nothing is given"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_max_integer_error_raised(self):
        """Test if nothing is given"""
        with self.assertRaises(Exception):
            max_integer(1)
