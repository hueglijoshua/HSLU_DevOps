class Word:
    def __init__(self, word):
        self.word = word.lower()
        self.correct_guesses = ["_"] * len(self.word)
        self.guessed_letters = set()

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print(f"Letter '{letter}' has already been guessed.")
            return False
        self.guessed_letters.add(letter)
        if letter in self.word:
            for idx, char in enumerate(self.word):
                if char == letter:
                    self.correct_guesses[idx] = letter
            return True
        return False

    def display_word(self):
        return " ".join(self.correct_guesses)

    def is_complete(self):
        return "_" not in self.correct_guesses

class Hangman:
    stages = [
        """
           ----
           |  |
           |
           |
           |
           |
        """,
        """
           ----
           |  |
           |  O
           |
           |
           |
        """,
        """
           ----
           |  |
           |  O
           |  |
           |
           |
        """,
        """
           ----
           |  |
           |  O
           | /|
           |
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\\
           |
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\\
           | /
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\\
           | / \\
        """
    ]

    def __init__(self):
        self.wrong_guesses = 0

    def draw(self):
        print(self.stages[self.wrong_guesses])

    def increment_wrong_guesses(self):
        self.wrong_guesses += 1
        if self.wrong_guesses >= len(self.stages) - 1:
            print("Game Over! The man has been hung.")
            return True
        return False

