import unittest
from Sort import Player


class TestSorting(unittest.TestCase):

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
