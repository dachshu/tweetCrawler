# FileRW
## Description
데이터 파일과 로그 파일에 읽고 쓰는 행동을 관리하는 클래스

## Variable
1. **data_file, log_file**  
데이터 파일 객체와 로그 파일 객체.
2. **account**  
입력된 계정 이름

## Function
1. **is_exist(name) -> (exist, last_id, last_time)**  
입력으로 들어온 계정에 대해서 Data와 Log가 존재하는지 확인하는 함수.
두 파일이 존재한다면 sync_between_data_log를 호출, 그렇지 않다면 파일을 생성한다.

2. **sync_between_data_log() -> last_id, last_time**  
Log에 있는 마지막 기록과 Data를 비교해서 무결성을 검증하는 함수.
Log에 기록되지 않는 트윗은 Data에서 제거한다.  
Data에 기록이 없으면 None을 반환하고, 기록이 있으면 마지막 기록 id와 unix_time을 반환한다.

3. **write_tweet(id, time, data)**  
tweet_id와 unix_time, html 데이터를 받아서 data_file과 log_file에 기록한다.