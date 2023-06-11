import unittest
import json
import os
from extensionNamer import extensionNamer

class TestGetName(unittest.TestCase):
    def setUp(self):
        with open("extensionNamer/extensionNames.json", "w") as f:
            json.dump({
                ".txt": "Text Document",
                ".doc": "Microsoft Word Document"
            }, f)

    def tearDown(self):
        os.remove("extensionNamer/extensionNames.json")

    def test_getName_withValidExtension(self):
        extension = ".txt"
        expected_name = "Text Document"
        actual_name = extensionNamer.getName(extension)
        self.assertEqual(actual_name, expected_name)

    def test_getName_withInvalidExtension(self):
        extension = ".invalid"
        expected_name = "Unknown"
        actual_name = extensionNamer.getName(extension)
        self.assertEqual(actual_name, expected_name)

    def test_getName_withFilePath(self):
        extension = "test.txt"
        expected_name = "Text Document"
        actual_name = extensionNamer.getName(extension)
        self.assertEqual(actual_name, expected_name)

if __name__ == "__main__":
    unittest.main()
