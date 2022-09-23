from google_news_feed import GoogleNewsFeed

gnf = GoogleNewsFeed(language='en',country='US') #setup


queryString = input('Enter search topic: ex \'McDonalds\'\n')
#asks for user input, what topic does the user want to search

results = gnf.query(queryString)
#sends a a request for RSS feed

print('printing the top 5 (out of 100) results:\n') #max length of a single query for RSS is 100 articles.

#len(results)
#this usually prints '100', unless there are not enough articles with that search term

for i in range(5): #supports up to 100 articles

    print(str(i) + '-th result below:')
    print('Title: ' + results[i].title)
    print('Link: ' + results[i].link)
    print('Date of article: ' + str(results[i].pubDate))
    print('Description: ' + results[i].description)
    print('Source: ' + results[i].source)
    print('\n')
