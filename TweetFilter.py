from bs4 import BeautifulSoup

class TweetFilter:
    def textFiltering(self, tweets):
        texts = []
        for tweet in tweets:
            soup = BeautifulSoup(tweet, 'html.parser')
            u_hidden = soup.findAll('a', {"class" : "u-hidden"})
            for element in u_hidden: element.extract()
            texts.append(soup.get_text())
        return texts



    def filtering(self, tweets, form):
        if form == 'text': return self.textFiltering(tweets)



html = """<p class="TweetTextSize  js-tweet-text tweet-text" data-aria-label-part="0" lang="en">The time has come to take action to IMPROVE access, INCREASE choices, and LOWER COSTS for HEALTHCARE! 
<img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/27a1.png" draggable="false" alt="➡️" title="Rightwards arrow" aria-label="Emoji: Rightwards arrow"><a href="https://t.co/mz5fdveTVh" rel="nofollow noopener" dir="ltr" data-expanded-url="http://45.wh.gov/Sp9y4H" class="twitter-timeline-link" target="_blank" title="http://45.wh.gov/Sp9y4H"><span class="tco-ellipsis"></span><span class="invisible">http://</span><span class="js-display-url">45.wh.gov/Sp9y4H</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a><a href="https://t.co/dDZLsKuNSe" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr">pic.twitter.com/dDZLsKuNSe</a></p>"""

t = []
t.append(html)

ft = TweetFilter()

l = ft.filtering(t, 'text')
for i in l:
    print(i)

"""
soup = BeautifulSoup(html, 'html.parser')

t = soup.findAll('a', {"class" : "u-hidden"})
print(len(t))
for element in t:
    element.extract()

print(soup.get_text())
"""