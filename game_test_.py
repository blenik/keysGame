import unittest
from InterfaceCreator import InterfaceCreator

class TestGame(unittest.TestCase):

    def test_point_increase(self):
        InterfacePrinter=InterfaceCreator()
        InterfacePrinter.points_increase(True)
        self.assertEqual(InterfacePrinter.p1Points, 1)
        self.assertEqual(InterfacePrinter.p2Points, 0)
        InterfacePrinter.points_increase(False)
        self.assertEqual(InterfacePrinter.p1Points, 1)
        self.assertEqual(InterfacePrinter.p2Points, 1)

    def test_point_decrease(self):
        InterfacePrinter=InterfaceCreator()
        InterfacePrinter.points_increase(True)
        InterfacePrinter.points_increase(False)

        InterfacePrinter.points_decrease(True)
        self.assertEqual(InterfacePrinter.p1Points, 0)
        self.assertEqual(InterfacePrinter.p2Points, 1)
        InterfacePrinter.points_decrease(True)
        self.assertEqual(InterfacePrinter.p1Points, 0)
        self.assertEqual(InterfacePrinter.p2Points, 1)

        InterfacePrinter.points_increase(True)

        InterfacePrinter.points_decrease(False)
        self.assertEqual(InterfacePrinter.p1Points, 1)
        self.assertEqual(InterfacePrinter.p2Points, 0)
        InterfacePrinter.points_decrease(False)
        self.assertEqual(InterfacePrinter.p1Points, 1)
        self.assertEqual(InterfacePrinter.p2Points, 0)


    def test_score_increase(self):
        InterfacePrinter=InterfaceCreator()
        self.assertEqual(InterfacePrinter.score, "|")
        InterfacePrinter.score_increase(True)
        self.assertEqual(InterfacePrinter.score, "*|")
        self.assertEqual(InterfacePrinter.p1Points, 0)
        self.assertEqual(InterfacePrinter.p2Points, 0)
        InterfacePrinter.score_increase(False)
        self.assertEqual(InterfacePrinter.score, "*|*")
        self.assertEqual(InterfacePrinter.p1Points, 0)
        self.assertEqual(InterfacePrinter.p2Points, 0)


    def test_line(self):
        InterfacePrinter=InterfaceCreator(40,"*")
        self.assertEqual(InterfacePrinter.line_breaker(), 40*"*"+"\n")
        self.assertEqual(InterfacePrinter.line_sides(), "*"+38*" "+"*\n")
        self.assertEqual(InterfacePrinter.line_score(), "*"+"SCORE".center(40-2*len("*"), ' ')+"*\n"
        "*"+"|".center(40-2*len("*"), ' ')+"*\n")
        self.assertEqual(InterfacePrinter.line_points(),"*P1"+(" "*(40-4-2*len("*")))+"P2*\n"
        "*"+str(0).zfill(3)+(" "*(40-6-2*len("*")))+str(0).zfill(3)+"*\n")
        


    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()