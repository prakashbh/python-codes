from bs4 import BeautifulSoup
import urllib.request

# Collect the relevant urls from the search engine for the
# user supplied keyword
def collect_urls():
    # Define and set an agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    # Accept a keyword from the user
    print("Enter the Keyword. [use - instead of space for more than one word]")
    key = input()

    # Prepare the search engine query
    # We are going to visit the google search engine
    # URL is prepared accordingly
    # Our result will be from the first page of the search engine only
    url = "http://www.google.com/search?q="+ key +"&start="

    # Open the page and parse through the BeautifulSoup
    # Parser is set to html. Any other suitable could be used as well
    page = opener.open(url)
    soup = BeautifulSoup(page, "html.parser")

    # Open a file and write all the links found
    file = open("links.txt", "w")
    for cite in soup.find_all('cite'):
        file.write(cite.text)
        file.write("\n")

    # Close the file
    file.close()

collect_urls()
