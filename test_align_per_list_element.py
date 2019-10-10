import unittest
from tools.file_input_output import read_from_file

class TEST_get_read_summary(unittest.TestCase):

    # just some test that does not make sense but only demonstrate how tests work
    def test_correct_input(self): # --> all test methods have to start with "test_"
        test_dic = ["some", "test", "list"]
        dic = []
        Type = type(test_dic)
        self.assertEqual(Type, type(dic))

class TEST_file_input_output(unittest.TestCase):

    def test_read_from_file(self):
        return
        # self.assertRaises(FileNotFoundError, read_from_file, input_file="/manuel/lol")

        # with self.assertRaises(FileNotFoundError):
        #     read_from_file(input_file="")

# now you can run all test from command line without saying "python3 -m unittest test_align_per_list_element.py"
# or directly within this IDE
if __name__ == '__main__':
    unittest.main()
