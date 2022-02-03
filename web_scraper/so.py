import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://stackoverflow.com/jobs?q=python"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


def get_last_page():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find("h3", {
        "class": "mb4"
    }).find_all("span", recursive=False)  # 첫번째 span만 가져오게 할 수 있다.
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']
    return {
        "title": title,
        "company": company,
        "location": location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
