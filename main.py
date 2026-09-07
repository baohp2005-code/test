import json
import random
from hangman_logic import HangmanGame

def load_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=== CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI ===")
    try:
        words_data = load_words("words.json")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file words.json")
        return

    topics = list(words_data.keys())

    while True:
        # A3: Cho phép người chơi chọn chủ đề
        print("\nCác chủ đề hiện có:")
        for i, topic in enumerate(topics):
            print(f"{i + 1}. {topic}")

        choice = input("Chọn chủ đề (nhập số): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
            continue

        selected_topic = topics[int(choice) - 1]
        word_list = words_data[selected_topic]
        
        # F1: Chọn ngẫu nhiên từ bí mật
        secret_word = random.choice(word_list)
        game = HangmanGame(secret_word)

        while not game.is_win() and not game.is_loss():
            # F2: Hiển thị trạng thái
            print("\n" + "="*30)
            print(f"Từ bí mật: {game.get_display_word()}")
            print(f"Các chữ đã đoán sai: {', '.join(game.wrong_guesses) if game.wrong_guesses else 'Chưa có'}")
            print(f"Số lượt còn lại: {game.get_remaining_tries()}")

            guess = input("Nhập 1 chữ cái: ").strip()
            status = game.process_guess(guess)

            # Xử lý thông báo không ảnh hưởng logic
            if status == "INVALID":
                print("Đầu vào không hợp lệ! Vui lòng chỉ nhập 1 chữ cái cái từ a-z.")
            elif status == "DUPLICATE":
                print("Bạn đã đoán chữ cái này rồi! Hãy thử chữ khác.")
            elif status == "CORRECT":
                print("Đoán đúng!")
            elif status == "WRONG":
                print("Đoán sai!")

        # F5: Kết thúc ván và hiển thị từ bí mật
        if game.is_win():
            print(f"CHÚC MỪNG! Bạn đã chiến thắng. Từ bí mật là: {game.secret_word}")
        else:
            print(f"GAME OVER! Bạn đã hết lượt đoán. Từ bí mật là: {game.secret_word}")

        # F5: Hỏi chơi lại
        play_again = input("\nBạn có muốn chơi lại không? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Cảm ơn bạn đã chơi. Hẹn gặp lại!")
            break

if __name__ == "__main__":
    main()