import unittest
from InterfaceCreator import InterfaceCreator

class TestInterface(unittest.TestCase):

    def test_point_increase(self):
        self.InterfacePrinter.points_increase(True)
        self.assertEqual(self.InterfacePrinter.p1Points, 1)
        self.assertEqual(self.InterfacePrinter.p2Points, 0)
        self.InterfacePrinter.points_increase(False)
        self.assertEqual(self.InterfacePrinter.p1Points, 1)
        self.assertEqual(self.InterfacePrinter.p2Points, 1)

    def test_point_decrease(self):
        self.InterfacePrinter.points_increase(True)
        self.InterfacePrinter.points_increase(False)

        self.InterfacePrinter.points_decrease(True)
        self.assertEqual(self.InterfacePrinter.p1Points, 0)
        self.assertEqual(self.InterfacePrinter.p2Points, 1)
        self.InterfacePrinter.points_decrease(True)
        self.assertEqual(self.InterfacePrinter.p1Points, 0)
        self.assertEqual(self.InterfacePrinter.p2Points, 1)

        self.InterfacePrinter.points_increase(True)

        self.InterfacePrinter.points_decrease(False)
        self.assertEqual(self.InterfacePrinter.p1Points, 1)
        self.assertEqual(self.InterfacePrinter.p2Points, 0)
        self.InterfacePrinter.points_decrease(False)
        self.assertEqual(self.InterfacePrinter.p1Points, 1)
        self.assertEqual(self.InterfacePrinter.p2Points, 0)


    def test_score_increase(self):
        self.assertEqual(self.InterfacePrinter.score, "|")
        self.InterfacePrinter.score_increase(True)
        self.assertEqual(self.InterfacePrinter.score, "*|")
        self.assertEqual(self.InterfacePrinter.p1Points, 0)
        self.assertEqual(self.InterfacePrinter.p2Points, 0)
        self.InterfacePrinter.score_increase(False)
        self.assertEqual(self.InterfacePrinter.score, "*|*")
        self.assertEqual(self.InterfacePrinter.p1Points, 0)
        self.assertEqual(self.InterfacePrinter.p2Points, 0)


    def test_line(self):
        self.assertEqual(self.InterfacePrinter.line_breaker(), 40*"*"+"\n")
        self.assertEqual(self.InterfacePrinter.line_sides(), "*"+38*" "+"*\n")
        self.assertEqual(self.InterfacePrinter.line_score(), "*"+"SCORE".center(40-2*len("*"), ' ')+"*\n"
        "*"+"|".center(40-2*len("*"), ' ')+"*\n")
        self.assertEqual(self.InterfacePrinter.line_points(),"*P1"+(" "*(40-4-2*len("*")))+"P2*\n"
        "*"+str(0).zfill(3)+(" "*(40-6-2*len("*")))+str(0).zfill(3)+"*\n")
        


    def setUp(self):
        self.InterfacePrinter=InterfaceCreator(40,"*")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()