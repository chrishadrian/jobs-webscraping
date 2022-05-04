import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd

conn = sqlite3.connect('jobs.db')
c = conn.cursor()
joblist = []

def extract(page):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}
    url = f"https://ca.indeed.com/jobs?q=software+engineer+intern&l=Vancouver%2C+BC&start={page}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def storeDB(title, company, location, date, summary):
    c.execute('''INSERT INTO jobs VALUES(?,?,?,?,?)''', (title, company, location, date, summary))
    conn.commit()

def storeCSV(title, company, location, date, summary):
    job = {
        'Title': title,
        'Company': company,
        'Location': location,
        'Date': date,
        'Summary': summary
        }
    joblist.append(job)

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

        storeDB(title, company, location, date, summary)
        storeCSV(title, company, location, date, summary)
    return

def main():
    try:
        c.execute('''DROP TABLE jobs''') ## delete table from database
    finally:
        c.execute('''CREATE TABLE jobs(Title TEXT, Company TEXT, Location TEXT, Date TEXT, Summary TEXT)''')

    # extract all pages
    for i in range(0, 40, 10):
        print(f'Getting page, {i}')
        c = extract(i)
        transform(c)

    # Saving data to csv file
    df = pd.DataFrame(joblist)
    df.to_csv('jobs.csv')
    # print(df.head())

    # Select which category in database to display in the db file
    c.execute('''SELECT * FROM jobs''')
    results = c.fetchall()
    print(results)

if __name__ == "__main__":
    main()
    

