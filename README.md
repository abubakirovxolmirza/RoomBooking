# Instalition
```bash
git clone https://github.com/abubakirovxolmirza/RoomBooking
```
```bash
docker build -t booking:1.0 .
docker run -p 1212:8000 booking:1.0
```

 HTTP so'rovlari va Javoblari

Ro’yxatini o'tish uchun `GET` :`…/api/register`
![img1](booking/media/readme_img/register.png)

Token olish uchun `GET` :`…/api/token`
![img1](booking/media/readme_img/token.png)

Tokenni kerakli joyga joylash
![img1](booking/media/readme_img/token1.png)

Tokenni saqlash
![img1](booking/media/readme_img/200.png)

Barcha xonalar ro’yxatini olish uchun uchun `GET` :`…/api/rooms`
![img1](booking/media/readme_img/rooms.png)

Xona haqida ma’lumot olish uchun `GET` → `…api/room/<room_name>`
![img1](booking/media/readme_img/lichniy.png)

Xonani bron qilish uchun esa `POST` `…/api/book/room`
![img1](booking/media/readme_img/book.png)

Agar unday hona yoq bo'lsa
![img1](booking/media/readme_img/error_book.png)

Agar band bo'lsa
![img1](booking/media/readme_img/drugoy.png)

