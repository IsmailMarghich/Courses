from bs4 import BeautifulSoup #import bs4 to extract pretty html
import requests #import requests to connect to a website
import pprint #import pretty print to print nice looking text
#the purpose of this program is to scrape news from hacker news with a certain about of points (upvotes)
res = requests.get('https://news.ycombinator.com/news') #request first page of hacker news
res2 = requests.get('https://news.ycombinator.com/news?p=2') #request the second page
soup = BeautifulSoup(res.text, 'html.parser') #parse both pages
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink') + soup2.select('.storylink') #combine the link of each story in a list
subtext = soup.select('.subtext') + soup2.select('.subtext') #combine the subtext class of each story, this will allow us to acces a lot of info from 1 select
def sort_stories_by_votes(hnlist): # this function will sort the dictionary we end up making later
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) #use a lambda function to sort the dictionary based on vote count, reverse it so highest comes first

def custom_hackernews(links, subtext): #define our function with the link and the subtext class
    hn = [] #create our list
    for index, item in enumerate(links): #for each item in the link, and we use enumerate and index so we can acces each article with its index in the list
        title = item.getText() #grab the title of the article
        href = item.get('href', None) #get the link via the 'href' tag
        vote = subtext[index].select('.score') #select the vote count by accessing each '.score' tag
        if len(vote): #make sure the article has a vote count, otherwise move on with the loop
            points = int(vote[0].getText().replace(' points', '')) #extract the numbers from the .score tag we scraped, and turn it into an integer
            if points > 99: #make sure its a popular article by only using articles with more than 99 votes
                hn.append({'title': title, 'link': href, 'votes': points}) #append to the list a dictionary with the title, link and points of an article
        
    return sort_stories_by_votes(hn) #return the list but first run it through the sorting function

pprint.pprint(custom_hackernews(links, subtext)) #pretty print the function and input our links and subtexts that we scraped.
