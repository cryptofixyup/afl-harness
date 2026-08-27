import unittest

from src.validation_pipeline import MAGIC, MAX_INPUT_SIZE, validate


class ValidationTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertFalse(validate(b"").valid)

    def test_magic_prefix(self):
        self.assertTrue(validate(MAGIC).valid)
        self.assertTrue(validate(MAGIC + b"payload").valid)

    def test_invalid_prefix(self):
        self.assertFalse(validate(b"invalid").valid)

    def test_size_limit(self):
        self.assertFalse(validate(b"x" * (MAX_INPUT_SIZE + 1)).valid)


if __name__ == "__main__":
    unittest.main()
