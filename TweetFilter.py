from bs4 import BeautifulSoup
import re

class TweetFilter:
    def textFiltering(self, tweets):
        texts = []
        for tweet in tweets:
            soup = BeautifulSoup(tweet, 'html.parser')
            u_hidden = soup.findAll('a', {"class" : "u-hidden"})
            for element in u_hidden: element.extract()
            texts.append(re.sub(r'\n{2,}','\n',soup.get_text()))
        return texts



    def filtering(self, tweets, form):
        if form == 'text': return self.textFiltering(tweets)
