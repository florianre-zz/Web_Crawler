from web_spider import WebSpider
from lxml import etree

def main():
    web_spider = WebSpider()
    links = web_spider.crawl('https://gocardless.com/')

    root = etree.Element('map')
    for link in links:
        child = etree.SubElement(root, 'url')
        child.text = link

    doc = etree.ElementTree(root)
    outFile = open('output.xml', 'wb')
    doc.write(outFile, xml_declaration=False, pretty_print=True)

main()
