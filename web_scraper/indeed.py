import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def get_last_page () :
  result = requests.get(URL)
  # indeed_result를 print시 작동된다는 뜻.
  # indeed_result.text print시 모든 html을 프린트한다.

  soup = BeautifulSoup(result.text, 'html.parser')
  # soup = BeautifulSoup(html_doc, 'html.parser')
  # 위에 쓰여진게 soup 공식인데, soup는 쉽게 말해 데이터를 분류해주는 역할을 한다.
  # 여기서 html_doc을 indeed_result.text 로 html document 를 가져와서 적어준것.

  pagination = soup.find("div", {"class" : "pagination"})
  # 페이지 관련 검사를 보면, div class="pagination"이 페이지를 나타낸다
  # 따라서 indeed_soup는 html을 가져왔으니까 여기서 find해라 어떤걸? div class pagination을 가진 정보들을 가져온다.

  links = pagination.find_all('a')
  # links는 pagination 변수 에서 find all 'a'를 찾아서 리스트를 만들어준것
  # 'a'는 페이지를 가르키는 html에서 2,3,4,5 페이지를 찾는것

  pages = []
  for link in links[:-1] :
    pages.append(int(link.string))
  # pages를 빈 리스트로 만들어주고 for문을 활용한다.
  # for문은 links 안에서 link라고하고 span을 찾아서 pages에 추가해라

  max_page = pages[-1]
  #max_page를 [-1]로 마지막 값만 나오게 지정
  return max_page

def extract_job(html):
  title = html.find("span", title=True).string
  company = html.find("span", {"class":"companyName"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = company.string
  location = html.find("div", {"class":"companyLocation"})
  if location is not None:
    location = location.string
  else:
    location = None

  job_id = html['data-jk']
  return {'title':title, 'company':company, 'location':location, 'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "fs-unmask"})
  for result in results:
    jobs.append(extract_job(result))
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs