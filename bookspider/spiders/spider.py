#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author:yclooper
from scrapy import Spider, Request
from bs4 import BeautifulSoup, SoupStrainer


class dingdianSpider(Spider):
    name = "dingdian"
    allowed_domins = ["www.x23us.com"]
    base_url = "http://www.x23us.com/class/"

    strainer = SoupStrainer("dl", id="content")

    def start_requests(self):
        for i in range(1, 11):
            url = self.base_url + str(i) + "_1.html"
            self.type = i
            yield Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml", from_encoding="utf-8", parse_only=self.strainer)

        page_count = soup.find("a", class_="last").get_text()

        print(page_count)
        for i in range(1, int(page_count) + 1):
            url = self.base_url + str(self.type) + "_" + str(i) + ".html"
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):

        soup = BeautifulSoup(response.text, "lxml", from_encoding="utf-8")

        book_node = soup.find_all("tr", bgcolor="#FFFFFF")
        for node in book_node:
            node_a = node.find_all("a")
            bk_url = node_a[0].get("href")
            bk_id = node_a[0].get("href").split("/")[-1]
            bk_name = node_a[1].get_text()

            node_tr = node.find_all("td", class_="C")

            bk_author = node_tr[0].get_text()
            bk_state = node_tr[-1].get_text()

            bk_count = node.find("td", class_="R").get_text()

            print(bk_name, bk_author, bk_state, bk_url, bk_count, bk_id)
