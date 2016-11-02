from web_spider import WebSpider
from lxml import etree

def main():
    web_spider = WebSpider()
    links = web_spider.crawl('https://gocardless.com/')

    tree = build_tree(links)
    doc = etree.ElementTree(root)
    outFile = open('output.xml', 'wb')
    doc.write(outFile, xml_declaration=False, pretty_print=True)

def build_tree((url, links_accessible_via_url)):
    root = etree.Element('url')
    for elem in links_accessible_via_url:
        if isinstance(elem, str)
            child = etree.SubElement(root, 'url')
            child.text = elem
        else
            root.append(build_tree(elem))

    return root

main()
