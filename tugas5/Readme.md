# Tugas 5 - Chatting

Implementasi chatting menggunakan socket dan thread.

Pertama, jalankan **server_thread_chat.py** agar server chat aktif.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas5/dokumentasi/server.png)

Lalu, jalankan **chat-cli.py** sebagai Client-side. 

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas5/dokumentasi/client.png)
Pada **chat.py**, sudah disediakan beberapa akun yang bisa melakukan chatting, yaitu **dwi**, **prasetya**, dan **armunanta** begitu juga dengan **passwordnya**.

Jika ingin chat, maka harus **login** terlebih dahulu.

## 1. Login
Untuk menjalankan fitur login, maka masukkan command: **auth [username] [password]**. Jika  akun tidak ada, maka akan error. Pilih salah satu dari ketiga akun yang telah disediakan.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas5/dokumentasi/login.png)

Pada contoh tersebut, saya login menggunakan username **dwi**.

## 2. Mengirim Pesan
Untuk melakukan pengiriman pesan, maka masukkan command **send [username-tujuan] [pesan]**. 

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas5/dokumentasi/send%20message.png)

Disini, saya ingin mengirim pesan ke **prasetya** dengan pesan **Halo Prasetya, ini pesan dari Dwi**. Maka saya menginputkan **send prasetya Halo Prasetya, ini pesan dari Dwi**. Jika berhasil maka akan ada notifikasi **message sent to prasetya**.

## 3. Melihat Pesan
Untuk melihat pesan yang masuk, maka lakukan command **inbox**.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas5/dokumentasi/check%20inbox.png)

Disini, saya ingin melihat pesan yang masuk ke **Prasetya**. Maka saya akan login ke **prasetya**. Lalu saya ketik **inbox**. Hasilnya adalah seperti gambar di atas.
