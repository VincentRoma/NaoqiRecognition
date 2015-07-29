from google_search import GoogleCustomSearch


SEARCH_ENGINE_ID = "006702229428365729256:bvi6g36u454"
API_KEY = "AIzaSyD_3bIA1h_-qETenJ3t1N2KKtU77z2n4MQ"

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)

for result in api.search('pdf', 'http://scraperwiki.com'):
    print(result['title'])
    print(result['link'])
    print(result['snippet']) 
