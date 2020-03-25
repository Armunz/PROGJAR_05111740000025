# Tugas 4 - Client-Server Request Respond

> PROTOCOL FORMAT  
  
> string terbagi menjadi 2 bagian, dipisahkan oleh spasi  
 COMMAND spasi PARAMETER spasi PARAMETER ...  
  
> FITUR  
  
> - download : untuk download file  
 request : download parameter : nama file response : berhasil -> ok gagal -> error  
>- upload : untuk upload file  
 request: upload parameter : nama file response: berhasil -> OK gagal -> ERROR  
>- list : untuk melihat daftar file  
 request: list parameter: tidak ada response: daftar record file yang ada  
>- jika command tidak dikenali akan merespon dengan ERRCMD


Pertama, jalankan **server_thread_file.py** agar server aktif.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/server-jalan.png)

Lalu jalankan **client.py**.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/client-jalan.png)

## Proses Download
Pada **client.py** inputkan string **download** dan **nama file** yang akan di download.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/download-process.png)

Hasilnya akan seperti berikut.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/hasil%20di%20client.png)

## Proses Upload
Pada **client.py** inputkan string **upload** dan pilih **nama file** yang akan di upload ke server.

Berikut hasilnya.

## Proses List
Pada **client.py** inputkan string **list** yang nantinya akan menampilkan list file yang ada pada server.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/list%20process.png)
Berikut hasilnya.

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas4/dokumentasi/hasil%20server.png)



