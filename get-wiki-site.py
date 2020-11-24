from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import argparse

def findParagraphTags(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(findParagraphTags, texts)
    return u" ".join(t.strip() for t in visible_texts)


def main(args):
    html = urllib.request.urlopen(args.wiki_side).read()
    output_path = args.output_path
    file = open(output_path, "w")
    file.write(text_from_html(html))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--wiki_side',
                        help='Webpage name to crawl', required=True)
    parser.add_argument('--output_path',
                        help='Path to the output file that D.A.V.E can learn something :) ', required=True)
    main()
