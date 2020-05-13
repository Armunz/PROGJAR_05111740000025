
# Apache Benchmark pada Asynchronous_Server_Thread dan Server_Thread dengan Load Balancer


Pertama, aktifkan dulu server-nya, lalu jalankan file **runserver.sh**, lalu jalankan **lb.py** (Load Balancer). Lalu akses http://localhost:44444/page.html.

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/page.html.png?raw=true)

Berikut log pada **lb.py**

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/log%20lb.py.png?raw=true)

Lalu testing Load Balancer menggunakan Apache Benchmark.

## Asynchronous_Server_Thread

### 1. 1000 Request 1 Concurrency

Command:

    ab -n 1000 -c 1 http://127.0.0.1:44444/

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%201.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%201%20%282%29.png?raw=true)

### 2. 1000 Request 10 Concurrency

Command:

       ab -n 1000 -c 10 http://127.0.0.1:44444/

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%2010.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%2010%20%282%29.png?raw=true)

### 3. 1000 Request 50 Concurrency

Command:

     ab -n 1000 -c 50 http://127.0.0.1:44444/

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%2050.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/-n%201000%20-c%2050%20%282%29.png?raw=true)

| Test | Concurrency Level | Time taken for test | Complete request | Failed Request | Total Transferred | Request Per Second | Time Per Request | Transfer Rate|
|--|--|--|--|--|--|--|--|--|
|1|1|0.860 second|1000|0|122000 bytes|1163.32 [#/sec] mean|0.860 [ms] (mean, across all concurrent request)|138.60 [KBytes/sec] received|
|2|10|0.426 second|1000|0|122000 bytes|2345.40 [#/sec] mean|0.426 [ms] (mean, across all concurrent request)|279.43 [KBytes/sec] received|
|3|50|1.098 second|1000|0|122000 bytes|910.84 [#/sec] mean|1.098 [ms] (mean, across all concurrent request)|108.52 [KBytes/sec] received|

Lalu, kita bandingkan dengan hasil dari **Server_Thread** biasa yang juga menggunakan load balancer.

## Server_Thread

### 1. 1000 Request 1 Concurrency
Command:

       ab -n 1000 -c 1 http://127.0.0.1:44444/

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%201.png)

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%201%20%282%29.png)

### 2. 1000 Request 10 Concurrency
Command:

       ab -n 1000 -c 10 http://127.0.0.1:44444/

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%2010.png)

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%2010%20%282%29.png)
### 3. 1000 Request 50 Concurrency
Command:

       ab -n 1000 -c 50 http://127.0.0.1:44444/

![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%2050.png)
![enter image description here](https://raw.githubusercontent.com/Armunz/PROGJAR_05111740000025/master/tugas10/dokum/server_thread/-n%201000%20-c%2050%20%282%29.png)

| Test | Concurrency Level | Time taken for test | Complete request | Failed Request | Total Transferred | Request Per Second | Time Per Request | Transfer Rate|
|--|--|--|--|--|--|--|--|--|
|1|1|0.926 second|1000|0|122000 bytes|1080.29 [#/sec] mean|0.926 [ms] (mean, across all concurrent request)|128.71 [KBytes/sec] received|
|2|10|0.513 second|1000|0|122000 bytes|1949.27 [#/sec] mean|0.513 [ms] (mean, across all concurrent request)|232.34 [KBytes/sec] received|
|3|50|0.471 second|1000|0|122000 bytes|2121.15 [#/sec] mean|0.471 [ms] (mean, across all concurrent request)|252.72 [KBytes/sec] received|

Ternyata, pada **Server_Thread** biasa, ketika menggunakan load balancer bisa menjalankan seluruh testing tanpa ada failed request.

