from textblob import TextBlob
from textblob.en import polarity
import tweepy
import sys

api_key = "V7oJ0v1NP1HS8siATK3S0Fs0c"
api_secret_key = "hEZO1fyNdSwRtUsteJmhRjCZK3ICUhHagFTUuI4AcQckilpwjF"
access_token = "1386599049294454787-L8jT2YTQlUAakhVrfSOhNe8xyl4i9D"
access_token_secret = "qHF0zcKxNg09gqydJTxYSxzITyO4JDJcKS6LpSLCDOQiO"

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = "dogecoin"

tweet_amount = 1000

tweets = tweepy.Cursor(api.search, q=search_term, lang="en").items(tweet_amount)

polarity = 0
positive = 0
neutral = 0
negative = 0

for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('#'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    if tweet_polarity == 0:
        neutral += 1
    if tweet_polarity < 0:
        negative += 1
    polarity += tweet_polarity

print('Positive count: ', positive)
print('Neutral count: ', neutral)
print('Negative count: ', negative)
print('Overall polarity: ', polarity)