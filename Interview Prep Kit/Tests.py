import unittest
from Sort import Player
from Sort import activity_notifications
from Sort import median
import numpy as np


class TestSortingActivityMonitor(unittest.TestCase):

    def test_activity_Notifications_SampleInput1_Returns2(self):
        expenditures = [10, 20, 30, 40, 50]
        trailing_days = 3

        self.assertEqual(1, activity_notifications(expenditures, trailing_days))

    def test_activity_Notifications_SampleInput2_Returns2(self):
        expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        trailing_days = 5

        self.assertEqual(2, activity_notifications(expenditures, trailing_days))

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

class TestSortingComparator(unittest.TestCase):

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
