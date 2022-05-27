# Data-Integration

## Bài tập quá trình
1. B1: Chạy file Dockerfile bằng lệnh "docker build -t kafka-spark-flink-example ." trong terminal
2. B2: Chạy file yml bằng docker-compose -f docker-compose.yml up
3. B3: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-producer_1 -f" để xem message gửi đến kafka queue
4. B4: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-consumer-spark_1 -f" để xem spark in ra chương trình wordcount đọc từ kafka queue xử lý trong 5s
5. B5: Sử dụng lệnh "docker logs kafka-spark-flink-example_kafka-consumer-flink_1 -f" để xem flink xử lý realtime liên tục chương trình wordcount.

```
Chú ý các tên file và tham số 5s hoàn toàn có thể cấu hình trong code được.
```



## BTL
1. B1: Chạy "docker build -t cluster-apache-spark ." để tạo image có tên cluster-apache-spark
2. B2: Chạy file yml bằng docker-compose filename.yml up từ kafka và spark
3. B3: Tạo ra các spider tương ứng với các nguồn mình crawl
4. B4: Định nghĩa các item và pipeline tương ứng và tạo topic theo từng nguồn, đẩy lên kafka
5. B5: Xem file test để hiểu hơn cách kết nối và đẩy dữ liệu
