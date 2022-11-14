from requests import get
from bs4 import BeautifulSoup



def get_job(lan):
  response = get(f"https://remoteok.com/remote-{lan}-jobs",
                 headers={"User-Agent": "HGJ"})
    print("Can't request website")
    
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('tr', class_="job")
    
    for job_section in jobs:
      companys = job_section.find_all('td', class_="company")
      
      for company in companys:
        company_anchors = company.find_all('a')
        
        for anchor in company_anchors:
          title = anchor.find('h2')
          
        company_spans = company.find_all('span')
        
        for span in company_spans:
          co = span.find('h3')
          
        if len(company.find_all('div', class_='location')) == 2:
          location, pay = company.find_all('div', class_='location')
          
        else:
          pay = company.find('div', class_='location')
          
      tags = job_section.find_all('td', class_="tags")
      
      for tag in tags:
        tag_anchor = tag.find('a')
        tag_div = tag_anchor.find('div')
        kind = tag_div.find('h3')
      
      job_data = {
        'title': title.string[1:-1].strip(),
        'company': co.string[1:-1].strip(),
        'region': location.string[2:].strip(),
        'position': kind.string[1:].strip(),
        'payment': pay.string[1:-1].strip()
      }
      
      results.append(job_data)
      
    for result in results:
      print(result)
      print('///////////////////////')


print("1.rust \n2.golang\n3.python\n4.react")
lan_num = int(input('Select Language : '))
lan = ['rust', 'golang', 'python', 'react']
get_job(lan[lan_num - 1])