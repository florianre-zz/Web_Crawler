import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

class WebSpider:

  def __init__(self, prohibited_domains=[]):
    self.visited = []
    self.prohibited_domains = prohibited_domains

  def crawl(self, start_url):
    links_in_url = []
    source_code = requests.get(start_url)
    soup = BeautifulSoup(source_code.text, "html.parser")

    for link in soup.findAll('a', attrs={'href' : re.compile("^[^\/]+\/[^\/].*$|^\/[^\/].*$")}):
      href = link.get('href')
      # TODO: do domain
      if href not in self.visited and href is not None:
        self.visited.append(href)
        href = str(href)
        complete_link = urljoin(start_url, href)
        print(complete_link)
        links_in_url.append(self.crawl(complete_link))

    return (start_url, links_in_url)
