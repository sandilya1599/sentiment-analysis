import tweepy
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def removeTagsAndLinks(tweet):
	cleaned_tweet=re.sub("@[A-Za-z0-9]+|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",tweet)
	return cleaned_tweet

#Tokenize the tweet. yes it is a spell error
def tokenise(tweet):
	cleaned_tweet=removeTagsAndLinks(tweet)
	sentences=sent_tokenize(cleaned_tweet)
	word=RegexpTokenizer(r'\w+')
	words=[word.tokenize(sentence) for sentence in sentences]
	#print(words)
	return words

# remove stopwords
def removeStopwords(tweet):
	stop_words=set(stopwords.words('english'))
	filtered_tweet=[word for dummytweet in tweet for word in  dummytweet  if word not in stop_words]
	#print(filtered_tweet)
	return filtered_tweet

def convert(tweet):
	converted_tweet=''
	for word in tweet:
		converted_tweet+=word+" "
	return converted_tweet
#authorize
def authorize():
	consumer_token="xxxxxxx"
	consumer_secret="xxxxxxxxxxxxxxxxxxxx"
	access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	auth=tweepy.OAuthHandler(consumer_token,consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api=tweepy.API(auth)
	return api
def analyze(query,limit=1000,language='en'):
	summary={'Positive':0,'Negitive':0,'Neutral':0}
	api=authorize()
	sid=SentimentIntensityAnalyzer()
	tweets=tweepy.Cursor(api.search,q=query,lang=language).items(limit)
	for tweet in tweets:
		tweet_text=tweet.text
		tweet=tokenise(tweet_text)
		tweet=removeStopwords(tweet)
		tweet=convert(tweet)
		score=sid.polarity_scores(tweet)
		if score['compound']==0:
			summary['Neutral']+=1
		elif score['compound']>0:
			summary['Positive']+=1
		else:
			summary['Negitive']+=1
	print('The tweets about the query %s are :'%query)
	for keys in summary.keys():
		print("No of %s tweets are %d"%(keys,summary[keys]))
#the main
def main():
	query=input('Enter the key to be searched:')
	no=int(input('Enter the number of tweets to be analyzed:'))
	try:
		language=input('Enter the language:')
	except:
		language='en'
	analyze(query,no,language)
if __name__=='__main__':
	main()