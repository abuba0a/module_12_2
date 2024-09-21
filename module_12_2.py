import HumanMoveTest
from unittest import TestCase


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = HumanMoveTest.Runner('Усэйн', 10)
        self.runner_2 = HumanMoveTest.Runner('Андрей', 9)
        self.runner_3 = HumanMoveTest.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            key_position = 1
            for key, value in test_value.items():
                key_position += 1

    def test_turn_1(self):
        turn_1 = HumanMoveTest.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    def test_turn_2(self):
        turn_2 = HumanMoveTest.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    def test_turn_3(self):
        turn_3 = HumanMoveTest.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')


TournamentTest()
