import TweetCrawler
import FileRW

file_manager = FileRW.FileRW()
tweetCrawler = TweetCrawler.TweetCrawelr()

account = input('account: ')
exist, last_id = file_manager.is_exist(account)
tweets = tweetCrawler.crawl(account, exist, last_id)
file_manager.write_tweet_list(tweets)