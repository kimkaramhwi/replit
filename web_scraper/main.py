from indeed import extract_indeed_pages
from indeed import extract_indeed_jobs

last_indeed_page = extract_indeed_pages()
jobs = extract_indeed_jobs(last_indeed_page)
print(jobs)