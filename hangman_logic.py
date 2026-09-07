class HangmanGame:
    def __init__(self, secret_word, max_failures=6):
        # F4: Không phân biệt hoa thường
        self.secret_word = secret_word.lower()
        self.max_failures = max_failures
        self.guessed_letters = set()
        self.wrong_guesses = set()

    def process_guess(self, char):
        # F3: Xử lý input không hợp lệ (chuỗi rỗng, >1 ký tự, không phải chữ cái)
        if not char or len(char) != 1 or not char.isalpha():
            return "INVALID"
        
        char = char.lower()
        
        # F3: Xử lý chữ đã đoán rồi
        if char in self.guessed_letters or char in self.wrong_guesses:
            return "DUPLICATE"

        if char in self.secret_word:
            self.guessed_letters.add(char)
            return "CORRECT"
        else:
            self.wrong_guesses.add(char)
            return "WRONG"

    def get_display_word(self):
        # Trả về trạng thái từ (VD: _ _ a _)
        return " ".join([c if c in self.guessed_letters else "_" for c in self.secret_word])

    def is_win(self):
        # Thắng khi đoán ra toàn bộ chữ cái
        return all(c in self.guessed_letters for c in self.secret_word)

    def is_loss(self):
        # Thua khi hết lượt
        return len(self.wrong_guesses) >= self.max_failures

    def get_remaining_tries(self):
        return self.max_failures - len(self.wrong_guesses)