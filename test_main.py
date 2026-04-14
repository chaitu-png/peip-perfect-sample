import unittest
from main import say_hello

class TestIntelligence(unittest.TestCase):
      def test_greeting_integrity(self):
                # Verifies the output matches professional standards
                self.assertEqual(say_hello(), "Hello, Predictive Engineering Intelligence Platform!")

  if __name__ == "__main__":
        unittest.main()
