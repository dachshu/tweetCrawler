# Tweet Crawler
## 개요
## 요구사항
- [python](https://www.python.org/) 3.5 이상
- [Selenium with python](http://selenium-python.readthedocs.io/)
- [Firefox](https://www.mozilla.org/ko/firefox/)
- [geckodriver](https://github.com/mozilla/geckodriver) (PATH에 등록되어있어야 함.)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
## 사용법
`python3`를 이용해서 `main.py`를 실행시키면 프로그램이 시작된다.

만약 이미 크롤링 했던 계정의 데이터가 남아있다면 자동으로 업데이트를 먼저 진행한다.

업데이트가 끝나거나 크롤링 했던 계정이 없다면 트윗을 크롤링하겠냐는 질문이 나온다. y를 선택한 경우 계정과 크롤링 시작 년,월을 입력받는다.

n을 선택해 크롤링을 하지 않으면 필터링 실행 여부를 묻는다. y를 눌러 필터링을 실행한 경우 저장된 트위터 계정과 필터링 포맷을 입력받는다. n을 선택해 필터링 하지 않는 경우, 프로그램이 종료된다.

필터링 포맷은 `text`, `time` 두가지가 있다. `text`는 트윗의 본문만 추출하고, `time`은 트윗이 작성된 시간을 unix time으로 추출한다.

필터링된 데이터는 `tweets/계정` 아래에 포맷에 따라 각각 `data_text`, `data_time`으로 저장된다.
## 예시
## TODO
## 참고