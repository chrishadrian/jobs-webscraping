import requests
from bs4 import BeautifulSoup

# access the webpage
result = requests.get("https://www.glassdoor.ca/member/home/companies.html")

# test the correctness of the website
# print(result.status_code)
# print(result.headers)

# store the page content to a variable
src = result.content

# parse and process the page content with a BeautifulSoup object
soup = BeautifulSoup(src, 'lxml')

# printing all the "a" properties
links = soup.find_all("a")
# print(links)
# print("\n")

# print with condition
for link in links:
    if "Salary" in link.text:
        print(link)
        print("\n")
        print(link.attrs['href'])