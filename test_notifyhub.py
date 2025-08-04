# test_notifyhub.py
"""
Tests for NotifyHub module.
"""

import unittest
from notifyhub import NotifyHub

class TestNotifyHub(unittest.TestCase):
    """Test cases for NotifyHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NotifyHub()
        self.assertIsInstance(instance, NotifyHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NotifyHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
