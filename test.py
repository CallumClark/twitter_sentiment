import tweepy
import csv
from textblob import TextBlob

consumer_key = 'YlPw8Q9RVn8xpP3L2S06MdZZy'
consumer_secret = 'NBVeulr3VMEXmvUp9yJRdAA4ie6s2Amdlc9pfe9s4BPuYkkI4S'

access_token = '4714670116-1xCjK1GZvNnAlQAtjlCd8lKdSj499jWlkkB0rqC'
access_token_secret = 'uM6W8pm5asZIqnAEYV7ROhWV1I9TwBNLjtDTwUVrLhGwO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#csvFile = open('Tweets.csv', 'a')
#csvWriter = csv.writer(csvFile)

public_tweets = api.search('Maastricht Uni')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)
#csvFile.close()