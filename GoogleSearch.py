# Create a python script called googlesearch that provides a command line utility to
# perform google search. It gives you the top links (search results) of whatever you want to
# search on google.

from googlesearch import search
def get_user_query():
    return input("Search on Google:  ")


def google_search(query):
    
    print(query)
    top_results = list(search(query, tld="com", num=10, stop=10))


    print(f"\nTop 10 results for '{query}':\n")
    for idx, result in enumerate(top_results, start=1):
        print(f"{idx}. {result}")


if __name__ == "__main__":
    user_query = get_user_query()
    google_search(user_query)
    
    
    