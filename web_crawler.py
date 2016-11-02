import requests
from bs4 import BeautifulSoup
from lxml import etree

def trade_spider():
    url = 'https://gocardless.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    visited = []
    home_page = '/'
    visited.append(home_page)
    for link in soup.findAll('a'):
        href = link.get('href')
        if href not in visited:
            visited.append(href)

    return visited

list = trade_spider()

root = etree.Element('map')
for link in list:
    child = etree.SubElement(root, 'url')
    child.text = link

doc = etree.ElementTree(root)
outFile = open('output.xml', 'wb')
doc.write(outFile, xml_declaration=False, pretty_print=True)
