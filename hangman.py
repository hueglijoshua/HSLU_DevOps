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