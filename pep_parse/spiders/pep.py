import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_tr_tags = response.css('section tbody tr')
        for pep_tr_tag in pep_tr_tags:
            pep_link = pep_tr_tag.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css('title::text').get()
        re_pattern = r'(?P<number>\d+) – (?P<name>.+) \| peps.python.org'

        pep_match = re.search(re_pattern, pep_info)
        number, name = pep_match.group('number', 'name')
        data = {
            'number': number,
            'name': name.strip(),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
