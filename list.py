Problems = [
    {
        "id": 1,
        "title": "Character Input",
        "description": "Tạo một chương trình với đầu vào là tên và tuổi của 1 người. In ra một thông báo cho biết năm người đó sẽ tròn 100 tuổi. Giả sử năm hiện tại là năm 2021. Thông báo trả về dạng: <name> will be 100 years old in the year <year>",
        "starter": "def charInput(name, age):\n\tpass",
        "passed": False
    },
    {
        "id": 2,
        "title": "Fibonacci",
        "description": "Viết chương trình với đầu vào n nguyên dương, trả về n số fibonacci đầu tiên (Chuỗi Fibonnaci là một dãy số trong đó số tiếp theo trong dãy là tổng của hai số trước đó trong dãy: 1, 1, 2, 3, 5, 8, 13,…).",
        "starter": "def fib(n):\n\tpass",
        "passed": False
    },
    {
        "id": 3,
        "title": "Rock Paper Scissors",
        "description": "Viết chương trình tạo trò chơi kéo búa bao (Rock Paper Scissors) với đầu vào u1, u2 là lựa chọn của mỗi người chơi (3 lựa chọn: 'rock', 'paper' và 'scissors'). Quy tắc: 'rock' win 'scissors' --> 'Rock wins!' , 'scissors' win 'paper' -->'Scissors win!', 'paper' win 'rock' --> 'Paper wins!', nếu trường hợp hòa --> 'It's a tie!', không trong 3 lựa chọn trên --> 'Try again! You have not entered rock, paper or scissors.'. return lại kết quả theo quy tắc đã cho ",
        "starter": "def compare(u1, u2):\n\tpass",
        "passed": False
    },
    {
        "id": 4,
        "title": "Divisors",
        "description": "Tạo một chương trình với đầu vào là một số và sau đó trả về danh sách tất cả các ước của số đó. ( Ví dụ: [1,2,13,26] là ước của 26.)",
        "starter": "def divisors(n):\n\tpass",
        "passed": False
    },
    {
        "id": 5,
        "title": "List Remove Duplicates",
        "description": "Viết chương trình (hàm!) Lấy một danh sách và trả về một danh sách mới chứa tất cả các phần tử của danh sách ban đầu bỏ đi đi tất cả các phần tử trùng lặp.",
        "starter": "def removeDuplicates(a):\n\tpass",
        "passed": False
    },
    {
        "id": 6,
        "title": "List Overlap",
        "description": "Lấy hai danh sách, chẳng hạn như hai danh sách sau: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]. Viết chương trình trả về một danh sách mới chỉ chứa các phần tử chung giữa 2 danh sách (không trùng lặp). Đảm bảo rằng chương trình của bạn hoạt động trên hai danh sách có kích thước khác nhau.",
        "starter": "def listOverlap(a,b):\n\tpass",
        "passed": False
    },
    {
        "id": 7,
        "title": "String Lists",
        "description": "Yêu cầu người dùng cung cấp một chuỗi gồm chữ hoặc số và trả về chuỗi này có phải là palindrome hay không (True or False). (Một palindrome là một chuỗi đọc tới và lùi như nhau. Ví dụ: ab5ba là 1 chuỗi palindrome.)",
        "starter": "def palindrome(string):\n\tpass",
        "passed": False
    },
    {
        "id": 8,
        "title": "Check Primality",
        "description": "Viết hàm nhận 1 số và kiểm tra xem số đó có phải là số nguyên tố hay không, trả về True hoặc False.(Số nguyên tố chỉ có 2 ước 1 và chính nó)",
        "starter": "def checkPrimality(num):\n\tpass",
        "passed": False
    },
    {
        "id": 9,
        "title": "Reverse Word Order",
        "description": "Viết một chương trình (sử dụng hàm!) với đầu vào cung cấp một chuỗi dài chứa nhiều từ. Trả về cho người dùng chuỗi có các từ theo thứ tự ngược lại. Ví dụ: 'My name is Michele' sẽ trả về chuỗi là 'Michele is name My' ",
        "starter": "def reverseWord(w):\n\tpass",
        "passed": False
    },
    {
        "id": 10,
        "title": "Birthday Dictionaries",
        "description": "Đối với bài tập này, chúng ta sẽ theo dõi ngày sinh của một người và có thể tìm thấy thông tin đó dựa trên tên của họ. Tạo một từ điển về tên và ngày sinh:'Albert Einstein': '03/14/1879', 'Benjamin Franklin': '01/17/1706', 'Ada Lovelace': '12/10/1815', 'Donald Trump': '06/14/1946', 'Rowan Atkinson': '01/6/1955'. Đầu vào của chương trình là tên và trả về ngày sinh của người đó '<name>'s birthday is <birthday>.'. Nếu không có trong từ điển, trả về 'Sadly, we don't have <name>'s birthday.'",
        "starter": "def birthdayDic(name):\n\tpass",
        "passed": False
    },
    {
        "id": 11,
        "title": "Calculate variance",
        "description": "Viết chương trình trả về giá trị trung bình, phương sai của  một danh sách các số thực. Giá trị trung bình là trung bình cộng của các giá trị trong danh sách. Phương sai tính bằng công thức <chèn image>. trong đó e là giá trị trung bình, xi là giá trị thứ i của danh sách.",
        "starter": "def variance(s):\n\tpass",
        "passed": False
    },
    {
        "id": 12,
        "title": "Divisible by 5",
        "description": "Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy. Ví dụ đầu vào là: 0100,0011,1010,1001 Đầu ra sẽ là: 1010",
        "starter": "def dec5(n):\n\tpass",
        "passed": False
    },
    {
        "id": 13,
        "title": "Make Dictionary",
        "description": "Nhập số nguyên dương từ bàn phím, hãy viết chương trình để tạo ra một dictionary chứa (i, và đảo ngược của i*i) với i là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó tả về dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 61, 5: 52, 6: 63, 7: 94, 8: 46}.",
        "starter": "def dictionary (n):\n\tpass",
        "passed": False
    }
]
