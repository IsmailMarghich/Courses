import unittest
import main
class TestMain(unittest.TestCase):
    def test_input(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result) #test wether the correct answer returns True
    def test_input_wrong_guess(self):
        result = main.run_guess(5, 0) #test wether the wrong answer returns False
        self.assertFalse(result)
    def test_input_wrong_number(self):
        result = main.run_guess(5, 11) #test wether an answer out of range for the game, returns False
        self.assertFalse(result)
    def test_input_wrong_type(self): #test wether an answer that is the wrong type (string), returns False
        result = main.run_guess(5, '11')
        self.assertFalse(result)
if __name__ == '__main__': #run the test if this is the main file
    unittest.main()
