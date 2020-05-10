
# Apache Benchmark pada Load Balancer Asynchronous_Server_Thread


Pertama, jalankan file **runserver.sh**, lalu jalankan **lb.py** (Load Balancer). Lalu akses http://localhost:44444/page.html.

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/page.html.png?raw=true)

Berikut log pada **lb.py**

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas10/dokum/log%20lb.py.png?raw=true)

Lalu testing Load Balancer menggunakan Apache Benchmark.

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
|3|10|1.098 second|1000|0|122000 bytes|910.84 [#/sec] mean|1.098 [ms] (mean, across all concurrent request)|108.52 [KBytes/sec] received|

Lalu, kita bandingkan dengan hasil dari **Server_Thread** biasa.
| Test | Concurrency Level | Time taken for test | Complete request | Failed Request | Total Transferred | Request Per Second | Time Per Request | Transfer Rate|
|--|--|--|--|--|--|--|--|--|
|1|1|431.036 second|1000|0|122000 bytes|2.32 [#/sec] mean|431.036 [ms] (mean, across all concurrent request)|0.28 [KBytes/sec] received|
|2|10|207.210 second|1000|0|122000 bytes|4.83 [#/sec] mean|207.210 [ms] (mean, across all concurrent request)|0.57 [KBytes/sec] received|
|3|50|-|963|37|-|-|-|-|

Ternyata, pada **Server_Thread** biasa, ketika menjalankan Test ketiga terjadi kegagalan request, karena memori yang digunakan telah penuh.
