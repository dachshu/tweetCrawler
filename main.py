import TweetCrawler
import FileRW

account = input('account: ')

file_manager = FileRW.FileRW()
tweetCrawler = TweetCrawler.TweetCrawelr()

exist, last_id = file_manager.is_exist(account)
tweets = tweetCrawler.crawl(account, exist, last_id)
file_manager.write_tweet_list(tweets)