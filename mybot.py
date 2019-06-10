import tweepy


print('this is my twitter bot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


public_tweets = api.home_timeline(count=2) #mira los tweets del timeline

for tweet in public_tweets: #bucle para los tweets del timeline

                #estos if creo que no funcionan    
    if tweet.in_reply_to_user_id== None and tweet.is_quote_status == False : 
        #escribo la respuesta a los tweets
        newtweet=api.update_status("@"+tweet.user.screen_name + " Ok, lo que tu digas", tweet.id)
        f= open("peopletofowllow.txt","a+")
        f.write(str(newtweet.id)+'\n')
        f.close() 
