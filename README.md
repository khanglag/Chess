# Chess

Chess là ứng dụng để chơi cờ. Giúp thư giãn sau giờ học.
Chess được phát triển bởi 2 thành viên:
  1. Nguyễn Kế Cường - Leader
  2. Đỗ Minh Khang - Thành viên


## Mục lục
- [Giới thiệu](#giới-thiệu)
- [Cài đặt](#cài-đặt)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)
- [Liên hệ](#liên-hệ)

## Giới thiệu
Chess được xây dựng hoàn toàn bằng python.
### Các thư viện sử dụng: 
  1. pickle.
  2. socket.
  3. threading
  4. pygame.
  5. engine
### Ứng dụng có 3 chế độ chơi:
  1. Chơi với bot.
  2. Chơi với người.
  3. Chơi với người nhưng hỗ trợ kết nối qua mạng LAN

## Cài đặt

#### 1. Cài đặt python
Trước tiên, hãy chắc chắn rằng bạn đã cài đặt Python trên máy tính của mình bằng cách mở mở cửa sổ Command Prompt (hoặc PowerShell) sau đó nhập dòng lệnh :
```bash
 python --version
 ```
Nếu chưa cài đặt , bạn có thể tải xuống phiên bản Python phù hợp với hệ điều hành của bạn từ trang web Python.org. (http://www.python.org/downloads/)

Sau khi tải xuống, nhấp đúp chuột vào tệp cài đặt và làm theo hướng dẫn để cài đặt Python. Đảm bảo bạn chọn tùy chọn “Add Python to PATH” để thêm Python vào biến môi trường PATH của bạn

Hướng dẫn cài đặt chi tiết : ( https://realpython.com/installing-python/ )

#### 2. Cài đặt pygame
Để có thể khởi tạo trò chơi ta cần phải cài đặt thư viện Pygame : Với Windows , mở cửa sổ Command Prompt (hoặc PowerShell) sau đó nhập dòng lệnh :
````bash
pip install pygame
````
#### 3. Clone repository về máy
```bash
https://github.com/khanglag/Chess.git
```
#### 4. Hướng dẫn chạy
##### 1. Chế độ chơi với bot
chạy file game.py và chọn chế độ chơi với bot
##### 2. Chế độ chơi với người
chạy file game.py và chọn chế độ chơi với người
##### 3. Chế độ chơi với người qua LAN
- Đảm bảo rằng 2 máy chơi kết nối chung 1 mạng LAN
- Sửa IP trong file game.py sao cho trỏ đúng IP server
###### Server
- Chạy server.py
- Lấy IP được in ra terminal nhập vào code game.py của cả 2 máy
###### Máy 1:
- Chạy game.py
- Chọn chế độ chơi với người qua mạng LAN
- Chọn cờ trắng
###### Máy 2:
- Chạy game.py
- Chọn chế độ chơi với người qua mạng LAN
- Chọn cờ đen
  
## Đóng góp
## Giấy phép
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Liên hệ
- Nguyễn Kế Cường - 3121410097
- Đỗ Minh Khang - 3121410007
