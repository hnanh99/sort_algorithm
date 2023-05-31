# sort_algorithm
Sort Algorithm (Các thuật toán sắp xếp)

1. Các hàm cần thiết
- Hàm đổi chỗ hai phần tử (swap.py)
- Hàm so sánh (compare.py)
- Hàm đọc file txt chứa mảng (read_file.py)
2. Sắp xếp nổi bọt (Burble Sort)
- Ý tưởng: Thuật toán sẽ đẩy các phần tử lớn xuống dưới mảng, các phần tử nhỏ hơn sẽ nổi lên dần dần (nổi bọt)
- Thuật toán: 
    - Duyệt từ phần tử đầu tiên
    - So sánh với phần từ liền trước nó, nếu phần tử trước lớn hơn phần tử sau thì đổi chỗ cho nhau
3. Sắp xếp chèn (Insertion Sort)
- Ý tưởng: Lấy ý tưởng từ việc chơi bài, dựa theo cách người chơi "chèn" thêm một quân bài mới vào bộ bài đã sắp xếp
- Thuật toán:
    - Duyệt từ phần tử đầu tiên
    - Từ phần tử thứ hai, chèn vào vị trí đúng, cứ thế đến hết mảng
