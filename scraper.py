import requests
from bs4 import BeautifulSoup

# access the webpage
result = requests.get("https://ca.indeed.com/jobs?q=software+engineer+intern&l=Vancouver%2C+BC")

# store the page content to a variable
src = result.content

# parse and process the page content with a BeautifulSoup object
soup = BeautifulSoup(src, 'html.parser')

# narrow down page content to jobcards
jobcards = soup.find_all('div', {"class":"job_seen_beacon"})

i = 0
for jobcard in jobcards:
    i += 1
print(i)

