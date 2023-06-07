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
4. Sắp xếp chọn (Selection Sort)
Thuật toán:
- Tìm phần tử nhỏ nhất đưa vào vị trí 1
- Tìm phần tử nhỏ tiếp theo đưa vào vị trí 2
- ...
5. Sắp xếp trộn (Merge Sort)
- Ý tưởng: Thuật toán chia để trị
- Thuật toán: 
    - Chia (Divide): Chia dãy gồm n phần tử cần sắp xếp thành 2 dãy, mỗi dãy có n/2 phần tử
    - Trị (Conquer): Sắp xếp mỗi dãy con một các đệ quy sử dụng sắp xếp trộn. Khi dãy chỉ còn một phần tử thì trả lại phần tử này
    - Tổ hợp (Combine): Trộn (Merge) hai dãy con được sắp xếp để thu được dãy được sắp xếp gồm tất cả các phần tử của cả hai dãy con
6. Sắp xếp nhanh (Quick Sort)
- Ý tưởng: theo thống kế tính toán
- Thuật toán: tương tự như Merge Sort, Quick Sort là thuật toán sắp xếp được phát triển dựa trên kỹ thuật chia để trị:
    - Neo đệ qui: Nếu dãy còn một phần tử thì nó là dãy đã sắp xếp
    - Chia (Divide):
        - Chọn một phần tử trong dãy và gọi nó là phần tử chốt p (pivot)
        - Chia dãy đã cho thành hai dãy con: Dãy bên trái (L) gồm những phần tử không lớn hơn phần tử chốt, còn dãy con phải (R) gồm các phần tử không nhỏ hơn phần tử chốt. Thao tác này được gọi là thao tác Phân đoạn (Partition)
    - Trị (Conquer): Lặp lại một cách đệ qui thuật toán với hai dãy con L và R
    - Tổng hợp (Combine): Dãy được sắp xếp là L q R
    
