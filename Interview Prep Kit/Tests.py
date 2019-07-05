from Sort import Player, activity_notifications, median
from LintChecks import check_bracket_consistency
from parameterized import parameterized
from GreedyAlgorithms import min_max
import unittest
import numpy as np


class TestLintChecks(unittest.TestCase):

    @parameterized.expand([
        ["([])[]({})", True],
        ["((()", False],
        ["([)]", False],
        ["{()[]([)}", False],
        ["{()[]([])}", True],
    ])
    def test_check_bracket_consistency(self, string, output):
        rv = check_bracket_consistency(string)
        self.assertEquals(rv, output)


class TestGreedyAlgorithms(unittest.TestCase):

    def test_max_min_example1(self):
        nums = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
        k = 4

        self.assertEqual(3, min_max(nums, k))

    def test_max_min_example2(self):
        nums = [10, 100, 300, 200, 1000, 20, 30]
        k = 3

        self.assertEqual(20, min_max(nums, k))

    def test_max_min_example3(self):
        nums = [100, 200, 300, 350, 400, 401, 402]
        k = 3

        self.assertEqual(2, min_max(nums, k))


    @unittest.skip("Demonstrating unit testing")
    def test_activity_Notifications_SampleInput1_Returns2(self):
        expenditures = [10, 20, 30, 40, 50]
        trailing_days = 3

        self.assertEqual(1, activity_notifications(expenditures, trailing_days))

    @unittest.skip("Demonstrating unit testing")
    def test_activity_Notifications_SampleInput2_Returns2(self):
        expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        trailing_days = 5

        self.assertEqual(2, activity_notifications(expenditures, trailing_days))

    @unittest.skip("Demonstrating unit testing")
    def test_activity_Notifications_SampleInput3_Returns2(self):
        expenditures = [1, 2, 3, 4, 4]
        trailing_days = 4

        self.assertEqual(0, activity_notifications(expenditures, trailing_days))

    def test_median_distribution_even(self):
        freq_distribution = np.array([1, 1, 0, 0, 1, 0, 1])

        self.assertEqual(2.5, median(freq_distribution))

    def test_median_distribution_odd(self):
        freq_distribution = np.array([1, 0, 1, 1, 2])

        self.assertEqual(3, median(freq_distribution))

    def test_comparator_WhenAScoresHigher_ReturnsNeg1(self):
        player_a = Player("Thomas", 100)
        player_b = Player("Wallner", 50)

        self.assertEqual(Player.comparator(player_a, player_b), -1)

    def test_comparator_WhenBScoresHigher_Returns1(self):
        player_a = Player("Thomas", 100)
        player_b = Player("Daniel", 200)

        self.assertEqual(Player.comparator(player_a, player_b), 1)

    def test_comparator_WhenAandBHaveSameScore_AndSameName_Returns0(self):
        player_a = Player("Thomas", 100)
        player_b = Player("Thomas", 100)

        self.assertEqual(Player.comparator(player_a, player_b), 0)

    def test_comparator_WhenAandBHaveSameScore_AndDifferentName_ReturnsNeg1(self):
        player_a = Player("Thomas", 100)
        player_b = Player("Wallner", 100)

        self.assertEqual(Player.comparator(player_a, player_b), -1)

    def test_comparator_WhenAandBHaveSameScore_AndDifferentName_Returns1(self):
        player_a = Player("Thomas", 0)
        player_b = Player("Daniel", 100)

        self.assertEqual(Player.comparator(player_a, player_b), 1)


if __name__ == '__main__':
    unittest.main()
