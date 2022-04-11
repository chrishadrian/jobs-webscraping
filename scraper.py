import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}
    url = f"https://ca.indeed.com/jobs?q=software+engineer+intern&l=Vancouver%2C+BC&start={page}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in divs:
        unwanted = item.find('span', class_ = 'visually-hidden')
        unwanted.extract()
        title = item.find('h2').text.strip()
        company = item.find('span', class_ = 'companyName').text.strip()
        location = item.find('div', class_ = 'companyLocation').text.strip()
        date = item.find('span', class_ = 'date').text.strip()
        summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n', '')

        job = {
            'title': title,
            'company': company,
            'location': location,
            'date': date,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = []

# extract all pages
for i in range(0, 40, 10):
    print(f'Getting page, {i}')
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')



# # store the page content to a variable
# src = result.content

# # parse and process the page content with a BeautifulSoup object
# soup = BeautifulSoup(src, 'html.parser')

# # narrow down page content to jobcards
# jobcards = soup.find_all('div', {"class":"job_seen_beacon"})

# i = 0
# for jobcard in jobcards:
#     i += 1
# print(i)

