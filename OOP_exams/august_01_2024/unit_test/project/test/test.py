from project.soccer_player import SoccerPlayer

import unittest


class TestSoccerPlayer(unittest.TestCase):

    def test_valid_initialization(self):
        player = SoccerPlayer(name="CristianoR", age=36, goals=100, team="Real Madrid")
        self.assertEqual(player.name, "CristianoR")
        self.assertEqual(player.age, 36)
        self.assertEqual(player.goals, 100)
        self.assertEqual(player.team, "Real Madrid")
        self.assertEqual(player.achievements, {})

    def test_invalid_name_short(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer(name="Ronal", age=20, goals=10, team="Barcelona")
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as context:
            SoccerPlayer(name="SomeoneElse", age=15, goals=5, team="Barcelona")
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

    def test_negative_goals_converts_to_zero(self):
        player = SoccerPlayer(name="LionelMessi", age=34, goals=-50, team="Barcelona")
        self.assertEqual(player.goals, 0)

    def test_invalid_team(self):
        with self.assertRaises(ValueError) as context:
            SoccerPlayer(name="AndresIniesta", age=30, goals=20, team="Random")
        expected_message = "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        self.assertEqual(str(context.exception), expected_message)

    def test_team_setter_valid(self):
        player = SoccerPlayer(name="CristianoR", age=36, goals=100, team="Real Madrid")
        player.team = "Juventus"
        self.assertEqual(player.team, "Juventus")

    def test_change_team_valid(self):
        player = SoccerPlayer(name="CristianoR", age=36, goals=100, team="Real Madrid")
        result = player.change_team("Juventus")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(player.team, "Juventus")

    def test_change_team_invalid(self):
        player = SoccerPlayer(name="LionelMessi", age=34, goals=700, team="Barcelona")
        result = player.change_team("NonExistent")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement_single(self):
        player = SoccerPlayer(name="LionelMessi", age=34, goals=700, team="Barcelona")
        result = player.add_new_achievement("Kicking")
        result2 = player.add_new_achievement("Kicking")
        self.assertEqual(result, "Kicking has been successfully added to the achievements collection!")
        self.assertEqual({"Kicking": 2}, player.achievements)

    def test_less_than_goals_of_another_player_returns_string(self):
        player1 = SoccerPlayer(name="LionelMessi", age=34, goals=700, team="Barcelona")
        player2 = SoccerPlayer(name="OtherPlayer", age=34, goals=800, team="Barcelona")

        result = player1.__lt__(player2)
        self.assertEqual(f"{player2.name} is a top goal scorer! S/he scored more than {player1.name}.", result)

    def test_more_than_goals_of_another_player_returns_string(self):
        player1 = SoccerPlayer(name="LionelMessi", age=34, goals=700, team="Barcelona")
        player2 = SoccerPlayer(name="OtherPlayer", age=34, goals=600, team="Barcelona")

        result = player1.__lt__(player2)
        self.assertEqual(f"{player1.name} is a better goal scorer than {player2.name}.", result)

    def test_eq_to_goals_of_another_player_returns_string(self):
        player1 = SoccerPlayer(name="LionelMessi", age=34, goals=700, team="Barcelona")
        player2 = SoccerPlayer(name="OtherPlayer", age=34, goals=600, team="Barcelona")

        result = player1.__lt__(player2)
        self.assertEqual(f"{player1.name} is a better goal scorer than {player2.name}.", result)






if __name__ == '__main__':
    unittest.main()


