# Apache Benchmark Server_Thread dan Asynchronous_Server_Thread

Disini saya menggunakan Jumlah request 1000 dan Concurrency 1, 10, 50.

## Server_Thread

### 1. 1000 Request 1 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/-n%201000%20-c%201.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/-n%201000%20-c%201%20%282%29.png?raw=true)

### 2. 1000 Request 10 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/-n%201000%20-c%2010.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/-n%201000%20-c%2010%20%282%29.png?raw=true)

### 3. 1000 Request 50 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/-n%201000%20-c%2050.png?raw=true)


| Test | Concurrency Level | Time taken for test | Complete request | Failed Request | Total Transferred | Request Per Second | Time Per Request | Transfer Rate|
|--|--|--|--|--|--|--|--|--|
|1|1|431.036 second|1000|0|122000 bytes|2.32 [#/sec] mean|431.036 [ms] (mean, across all concurrent request)|0.28 [KBytes/sec] received|
|2|10|207.210 second|1000|0|122000 bytes|4.83 [#/sec] mean|207.210 [ms] (mean, across all concurrent request)|0.57 [KBytes/sec] received|
|3|50|-|963|37|-|-|-|-|

## Asynchronous_Server_Thread

### 1. 1000 Request 1 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%201.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%201%20%282%29.png?raw=true)

### 2. 1000 Request 10 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%2010.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%2010%20%282%29.png?raw=true)

### 3. 1000 Request 50 Concurrency

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%2050.png?raw=true)

![enter image description here](https://github.com/Armunz/PROGJAR_05111740000025/blob/master/tugas9/dokum/async/-n%201000%20-c%2050%20%282%29.png?raw=true)

| Test | Concurrency Level | Time taken for test | Complete request | Failed Request | Total Transferred | Request Per Second | Time Per Request | Transfer Rate|
|--|--|--|--|--|--|--|--|--|
|1|1|0.355 second|1000|0|122000 bytes|2816.41 [#/sec] mean|0.355 [ms] (mean, across all concurrent request)|335.56 [KBytes/sec] received|
|2|10|0.318 second|1000|0|122000 bytes|3147.73 [#/sec] mean|0.318 [ms] (mean, across all concurrent request)|375.02 [KBytes/sec] received|
|3|10|0.288 second|1000|0|122000 bytes|3471.45 [#/sec] mean|0.288 [ms] (mean, across all concurrent request)|413.59 [KBytes/sec] received|
