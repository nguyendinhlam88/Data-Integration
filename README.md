# Data-Integration

## Bài tập quá trình
B1: Chạy file Dockerfile bằng lệnh "docker build -t kafka-spark-flink-example ." trong terminal
B2: Chạy file yml bằng docker-compose -f docker-compose.yml up
B3: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-producer_1 -f" để xem message gửi đến kafka queue
B4: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-consumer-spark_1 -f" để xem spark in ra chương trình wordcount đọc từ kafka queue xử lý trong 5s
B5: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-consumer-flink_1 -f" để xem flink xử lý realtime liên tục chương trình wordcount.

```
Chú ý các tên file và tham số 5s hoàn toàn có thể cấu hình trong code được.
```



## BTL
B1: Chạy file yml bằng docker-compose filename.yml up từ kafka và spark
B2: Tạo ra các spider tương ứng với các nguồn mình crawl
B3: Định nghĩa các item và pipeline tương ứng và tạo topic theo từng nguồn, đẩy lên kafka
B4: Xem file test để hiểu hơn cách kết nối và đẩy dữ liệu