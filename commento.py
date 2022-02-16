#! /usr/bin/python3

import requests
import re
import threading # implement threading for faster link finding


HOST_URL = ""
ALL_LINKS = []
LINK_REGEX_PATTERN = "^https://\w+"
HTML_COMMENT_REGEX_PATTERNS = [] # list of all the diff language comments
JS_COMMENT_REGEX_PATTERNS = []   # list of all the js langugae comments


def crawl_site() -> str:
    ''' Crawls the webiste to find for http links'''
    # TODO: find a way to integrate with directory busting tools
    # TODO: Find integration with the wayback machine and parse the links to crawl
    try:
        req = requests.get(HOST_URL) # request the homepage of the site and find links
        # in_scope = re.match(HOST_URL) # find a way to exclude out-of-scope links
        haystack = req.text
        needles = re.findall(REGEX_PATTERN, haystack)
    except Exception as error:
        print(error)


def main():
    crawl_site()


if __name__ == '__main__':
    main()
