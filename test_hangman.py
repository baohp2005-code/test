import unittest
from hangman_logic import HangmanGame

class TestHangmanGame(unittest.TestCase):
    def test_doan_dung(self):
        game = HangmanGame("hello")
        res = game.process_guess("e")
        self.assertEqual(res, "CORRECT")
        self.assertIn("e", game.guessed_letters)
        self.assertEqual(game.get_remaining_tries(), 6)

    def test_doan_sai(self):
        game = HangmanGame("hello")
        res = game.process_guess("z")
        self.assertEqual(res, "WRONG")
        self.assertIn("z", game.wrong_guesses)
        self.assertEqual(game.get_remaining_tries(), 5)

    def test_doan_trung(self):
        game = HangmanGame("hello")
        game.process_guess("e")
        res = game.process_guess("e")
        self.assertEqual(res, "DUPLICATE")
        # Không bị trừ lượt
        self.assertEqual(game.get_remaining_tries(), 6) 

    def test_thang_game(self):
        game = HangmanGame("cat")
        game.process_guess("c")
        game.process_guess("a")
        game.process_guess("t")
        self.assertTrue(game.is_win())
        self.assertFalse(game.is_loss())

    def test_thua_game(self):
        game = HangmanGame("cat", max_failures=2)
        game.process_guess("z")
        game.process_guess("x")
        self.assertFalse(game.is_win())
        self.assertTrue(game.is_loss())

if __name__ == '__main__':
    unittest.main()