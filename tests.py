import unittest
import functions


class test_traverse_directory(unittest.TestCase):
    def test1_success(self):
        self.assertEqual(
            functions.traverse_directory('./tests/test-1'),
            [['./tests/test-1/test1.txt', './tests/test-1/Folder-1/test2.txt']],
        )

    def test2_success(self):
        self.assertEqual(
            functions.traverse_directory('./tests/test-2'),
            [
                [
                    './tests/test-2/Duplicate-1.json',
                    './tests/test-2/Duplicate-2.txt',
                    './tests/test-2/directory-1/directory-2/Duplicate-3.json',
                    './tests/test-2/directory-1/directory-2/directory-3/Duplicate-4.json',
                ]
            ],
        )


if __name__ == '__main__':
    unittest.main()
