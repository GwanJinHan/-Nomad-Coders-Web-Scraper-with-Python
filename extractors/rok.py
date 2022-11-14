from requests import get
from bs4 import BeautifulSoup


def extract_rok_jobs(keyword):
  response = get(f"https://remoteok.com/remote-{keyword}-jobs",
                 headers={"User-Agent": "HGJ"})
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    trs = soup.find_all("tr", {"class": "job"})

    for tr in trs:
      title = tr.find("h2").string
      company = tr.find("h3").string
      location = tr.find("div", {"class": "location"}).string
      link = tr.find("a", {"itemprop": "url"})["href"]

      job_data = {
        "link": f"https://remoteok.com{link}".replace("\n", ""),
        "company": company.replace("\n", ""),
        "location": location.replace("\n", ""),
        "position": title.replace("\n", ""),
      }
      for data in job_data:
        if job_data[data] != None:
          job_data[data] = job_data[data].replace(",", " ")

      results.append(job_data)
    return results