import TweetCrawler

tweetCrawler = TweetCrawler.TweetCrawelr()

tweetCrawler.update()

while True:
    a = input("트윗 크롤링 실행? ")
    if( a =='y' or a == 'yes'):
        account = input('account: ')
        join_year = input('join year: ')
        join_month = input('join month: ')
        tweetCrawler.crawling(account, int(join_year), int(join_month))
    else: break