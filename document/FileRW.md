# FileRW
## Description
데이터 파일과 로그 파일에 읽고 쓰는 행동을 관리하는 클래스
## Variable
1. **data_file, log_file**<br>
데이터 파일 객체와 로그 파일 객체.
## Function
1. **IsExist(name) -> exist, last_time**<br>
입력으로 들어온 ID에 대해서 Data와 Log가 존재하는지 확인하는 함수.
두 파일이 존재한다면, 파일을 열어서 data_file 변수와 log_file 변수에 저장하고 SyncBetweenDataLog을 호출.

2. **SyncBetweenDataLog()**<br>
Log에 있는 마지막 기록과 Data를 비교해서 무결성을 검증하는 함수.
Log에 기록되지 않는 트윗은 Data에서 제거한다.

3. **WriteTweet(time, data)**<br>
시간과 html 데이터를 받아서 data_file과 log_file에 기록한다.