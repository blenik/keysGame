import unittest
from fight import Fight_Class


class TestFightModule(unittest.TestCase):


    def test_collision(self):

        self.assertTrue(self.testClass.collision(1, 1, 2, 1))
        self.assertFalse(self.testClass.collision(1, 1, 3, 5))
        self.assertTrue(self.testClass.collision(2, 2, 2, 3))
        self.assertFalse(self.testClass.collision(4, 5, 3, 4))

    def test_display_letters(self):
        self.assertEqual(self.testClass.display_letters_toclick(['x', 'z', 'c'], ['b', 'n', 'm']),"Player 1: x z c \tPlayer 2: b n m ")
        self.assertEqual(self.testClass.display_letters_toclick(['z', 'x', 'c'], ['b', 'm', 'n']),"Player 1: z x c \tPlayer 2: b m n ")
        self.assertEqual(self.testClass.display_letters_toclick(['c', 'z', 'x'], ['m', 'n', 'b']),"Player 1: c z x \tPlayer 2: m n b ")
        self.assertEqual(self.testClass.display_letters_toclick(['x', 'c', 'z'], ['n', 'b', 'm']),"Player 1: x c z \tPlayer 2: n b m ")

    def setUp(self):
        self.testClass = Fight_Class()

if __name__ == '__main__':
    unittest.main()