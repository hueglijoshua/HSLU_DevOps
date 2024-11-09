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


class Game:
    def __init__(self):
        # The word is entered by the user at the start of the game
        self.word = self.get_word_from_player()
        self.word = Word(self.word) 
        self.hangman = Hangman()

    def get_word_from_player(self):
        word = input("Enter the word for the game (Player 1): ").strip()
        # Make sure the word is non-empty and consists of letters only
        while not word.isalpha() or len(word) == 0:
            print("Please enter a valid word (letters only).")
            word = input("Enter the word for the game (Player 1): ").strip()
        return word

    def play(self):
        print("Welcome to Hangman!")
        while True:
            print("\nCurrent word:", self.word.display_word())
            print("Missed letters:", " ".join(sorted(self.word.guessed_letters - set(self.word.correct_guesses))))
            self.hangman.draw()
            letter = input("Guess a letter: ").lower()

            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single alphabetic character.")
                continue

            if not self.word.guess_letter(letter):
                if self.hangman.increment_wrong_guesses():
                    break
            elif self.word.is_complete():
                print("Congratulations! You've guessed the word:", self.word.word)
                break


# Usage
game = Game()  # Now, the word is entered at the start
game.play()
