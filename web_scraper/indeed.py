import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    #max_page를 [-1]로 마지막 값만 나오게 지정
    return max_page


def extract_job(html):
    title = html.find("span", title=True).string
    company = html.find("span", {"class": "companyName"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
    else:
        company = None

    location = html.find("div", {"class": "companyLocation"})
    if location is not None:
        location = location.string
    else:
        location = None

    job_id = html['data-jk']
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed: Page {page}")
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
