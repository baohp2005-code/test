# test
Dự án Trò chơi Đoán chữ (Hangman)

1. Giới thiệu

Đây là phiên bản trò chơi đoán chữ (Hangman) kinh điển được phát triển bằng Python. Dự án được thiết kế theo hướng module hóa, đảm bảo mã nguồn gọn gàng, dễ bảo trì và đáp ứng các tiêu chuẩn cơ bản của phát triển phần mềm.

2. Hướng dẫn cài đặt và chạy game

Yêu cầu hệ thống: Python 3.x trở lên

Cách chạy:

Đảm bảo bạn đã lưu 4 file (words.json, hangman_logic.py, test_hangman.py, main.py) vào cùng một thư mục.

Mở Terminal (macOS/Linux) hoặc Command Prompt/PowerShell (Windows).

Di chuyển (cd) đến thư mục chứa mã nguồn.

Khởi động trò chơi bằng lệnh:

python main.py


3. Hướng dẫn chạy Unit Test

Dự án bao gồm một bộ kiểm thử tự động (Unit Test) cho phần cốt lõi của trò chơi để đảm bảo tính chính xác của các quy tắc (đoán đúng, đoán sai, kiểm tra điều kiện thắng/thua).

Để chạy bộ Unit Test, hãy thực thi lệnh sau:

python -m unittest test_hangman.py


4. Các quyết định thiết kế

Trong quá trình xây dựng, dự án áp dụng các quyết định thiết kế cốt lõi sau:

Tách biệt hoàn toàn Game Logic và UI: Đây là quyết định quan trọng nhất. Phần xử lý luật chơi (hangman_logic.py) được thiết kế độc lập, không sử dụng bất kỳ hàm print() hay input() nào. Điều này giúp logic game dễ dàng được kiểm thử tự động và có thể tái sử dụng nguyên vẹn nếu sau này nâng cấp lên giao diện Web hoặc Desktop.

Xử lý ngoại lệ chặt chẽ: Các trường hợp người chơi vô tình hoặc cố ý nhập sai (để trống, nhập nhiều ký tự, ký tự đặc biệt, hoặc đoán lại chữ đã từng đoán) đều được hệ thống chặn lại mà không làm chương trình bị crash và không trừ lượt của người chơi.

Cấu trúc dữ liệu linh hoạt: Sử dụng file JSON để lưu trữ từ vựng theo chủ đề, giúp dễ dàng thêm bớt từ hoặc chủ đề mới mà không cần can thiệp vào code logic.

5. Các tính năng có thể phát triển trong tương lai (Future Improvements)

Nếu có thêm thời gian, dự án có thể được mở rộng với các tính năng sau:

Tùy chọn mức độ khó: Bổ sung các mức Dễ / Trung bình / Khó, ảnh hưởng trực tiếp đến số lượng lượt đoán sai cho phép hoặc độ dài của từ bí mật.

Hệ thống gợi ý (Hint): Cho phép người chơi lật mở ngẫu nhiên 1 chữ cái, đánh đổi bằng việc bị trừ đi 1 hoặc 2 lượt đoán.

Điểm số & Lưu trữ: Xây dựng hệ thống tính điểm dựa trên số lượt đoán còn lại và lưu trữ bảng xếp hạng người chơi qua các phiên bản.

Giao diện đồ họa (GUI): Nâng cấp lên giao diện Desktop (Tkinter/PyQt) hoặc giao diện Web để tăng trải nghiệm người dùng thay cho giao diện Console hiện tại.
