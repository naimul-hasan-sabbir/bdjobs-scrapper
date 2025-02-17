from bs4 import BeautifulSoup
import requests

response = requests.get("https://jobs.bdjobs.com/jobsearch.asp?log=stats")
soup = BeautifulSoup(response.content, "html.parser")

#print(soup)
job_listings = soup.find_all(name="div", class_="title")

job_titles = []

for job_listing in job_listings:
    title = job_listing.find(name="a")
    job_titles.append(title.getText().strip())

print(job_titles)