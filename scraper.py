import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = “https://www.indeed.co.uk/jobs?q=restaurant&l=England"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, “html.parser”)
#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())

def extract_job_title_from_result(soup): 
  jobs = []
    for div in soup.find_all(name=”div”, attrs={“class”:”row”}):
      for a in div.find_all(name=”a”, attrs={“data-tn-element”:”jobTitle”}):
      jobs.append(a[“title”])
  return(jobs)
extract_job_title_from_result(soup)
