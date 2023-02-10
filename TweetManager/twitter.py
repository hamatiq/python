from tweet import Tweet
import pickle
file = open('tweets.dat','rb')
try:
    tweets = pickle.load(file)
except EOFError:
    tweets = []
file.close()

while (True):
    print('\nTweet Menu\n-—————')
    i = input("1. Make a Tweet\n2. View Recent Tweets\n3. Search Tweets\n4. Quit\n\nWhat would you like to do?")

    if(i == '1'):
        auther = input('What is your name? ')
        text = input('What would you like to tweet: ')
        tweets.append(Tweet(auther,text))
        try:
            file = open('tweets.dat','wb')
            pickle.dump(tweets,file)
            file.close()
            print(auther + ', your tweet has been saved.')
        except:
            print('Something went wrong try again!  :(')

    elif(i == '2'):
        print ( 'Recent Tweets\n-——————')
        if (len(tweets) == 0):
            print ( 'no recent tweets! ;) ')
            
        else:
            for t in tweets:
                t.print_tweet()

    elif(i == '3'):
        inp = input( 'What would you like to search for? ')
        ftweet = []
        for t in tweets:
            if (((t.get_text()).find(inp))!= -1):
                ftweet.append(t)
        if (len(ftweet) == 0 ):
            print("No match was found!  ;(\n")
        else:
            ftweet.sort(key=lambda x: x.get_age(), reverse=False)
            for tweet in ftweet:
                tweet.print_tweet()

    elif(i == '4'):
        print('exit')
        break

    else:
        print('Input not valid please trry again!\n')