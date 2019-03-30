# Sentiment Analysis on Twitter Tweets

Sentiment Analysis refers to the use of Natural Language Processing, Text Analysis, Computer Linguistics to identify, extract, study the opinions and affective states.

Here, we are applying Sentiment Analysis on twitter's tweets.

## Requirements

NLTK - [Link](https://www.nltk.org/)
Tweepy - [Link](http://www.tweepy.org/)
Python 3.6

### Implementation Details

First we get the tweets from Twitter using Tweepy API. After obtaining the tweets, we preprocess each tweet. For Preprocessing, we remove the hyperlinks and special characters. Then for removing the stopwords we tokenize the tweet and remove the stopwords. After removing the stopwords, we use vader in NLTK to find the polarity of the tweet. We classify it as positive or negitive or neutral.


### References

[FCPython](https://fcpython.com/blog/scraping-twitter-tweepy-python)
[GeeksForGeeks](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/)

