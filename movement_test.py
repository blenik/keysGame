import unittest
from movement import player


class MovementTest(unittest.TestCase):

    def test_move_up(self):
        self.assertEqual(self.play.move_up(self.plansza), False)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
        self.assertEqual(self.play.move_up(self.plansza), True)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
        self.assertEqual(self.play.move_up(self.plansza), False)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
    def test_move_down(self):
        self.assertEqual(self.play.move_down(self.plansza), False)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
        self.assertEqual(self.play.move_down(self.plansza), True)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
        self.assertEqual(self.play.move_down(self.plansza), False)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "p", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])

    def test_move_right(self):
        self.assertEqual(self.play.move_right(self.plansza), False)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", "p","k", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])
        self.assertEqual(self.play.move_right(self.plansza), True)
        self.assertEqual(self.plansza, [["#","#", "#", "#", "#","#", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#","k", " ", " ", " ","p", "#"],
                                        ["#"," ", " ", " ", " "," ", "#"],
                                        ["#"," ", " ", "k", " "," ", "#"],
                                        ["#","#", "#", "#", "#","#", "#"]
                                        ])

        self.assertEqual(self.play.move_right(self.plansza), False)
        self.assertEqual(self.plansza, [["#", "#", "#", "#", "#", "#", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", "k", " ", " ", " ", "p", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", "#", "#", "#", "#", "#", "#"]
                                        ])

    def test_move_left(self):
        self.assertEqual(self.play.move_left(self.plansza), False)
        self.assertEqual(self.plansza, [["#", "#", "#", "#", "#", "#", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", "k", "p", " ", " ", "k", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", "#", "#", "#", "#", "#", "#"]
                                        ])
        self.assertEqual(self.play.move_left(self.plansza), True)
        self.assertEqual(self.plansza, [["#", "#", "#", "#", "#", "#", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", "p", " ", " ", " ", "k", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", "#", "#", "#", "#", "#", "#"]
                                        ])

        self.assertEqual(self.play.move_left(self.plansza), False)
        self.assertEqual(self.plansza, [["#", "#", "#", "#", "#", "#", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", "p", " ", " ", " ", "k", "#"],
                                        ["#", " ", " ", " ", " ", " ", "#"],
                                        ["#", " ", " ", "k", " ", " ", "#"],
                                        ["#", "#", "#", "#", "#", "#", "#"]
                                        ])

    def setUp(self):
        self.plansza = [["#","#", "#", "#", "#","#", "#"],
                        ["#"," ", " ", "k", " "," ", "#"],
                        ["#"," ", " ", " ", " "," ", "#"],
                        ["#","k", " ", " ", " ","k", "#"],
                        ["#"," ", " ", " ", " "," ", "#"],
                        ["#"," ", " ", "k", " "," ", "#"],
                        ["#","#", "#", "#", "#","#", "#"]
                        ]
        self.play =player(3, 3,self.plansza,"p")


if __name__ == '__main__':
    unittest.main()
