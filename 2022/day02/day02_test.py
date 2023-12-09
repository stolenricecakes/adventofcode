import unittest
import day02

class TestDay02Methods(unittest.TestCase):

    def test_X_part2_score(self):
        self.assertEqual(day02.part2_calc_score("X"), 0)

    def test_Y_part2_score(self):
        self.assertEqual(day02.part2_calc_score("Y"), 3)

    def test_Z_part2_score(self):
        self.assertEqual(day02.part2_calc_score("Z"), 6)

    def test_A_X_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("A", "X"), 3)

    def test_A_Y_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("A", "Y"), 1)

    def test_A_Z_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("A", "Z"), 2)

    def test_B_X_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("B", "X"), 1)

    def test_B_Y_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("B", "Y"), 2)

    def test_B_Z_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("B", "Z"), 3)

    def test_C_X_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("C", "X"), 2)

    def test_C_Y_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("C", "Y"), 3)

    def test_C_Z_part2_hand(self):
        self.assertEqual(day02.part2_calc_throw("C", "Z"), 1)



if __name__ == '__main__':
    unittest.main()