import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    END_NAME, MID_SEP, SPIDER_NAME, SPIDER_PEP_URL, START_NAME
)


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = [SPIDER_PEP_URL]
    start_urls = [f'https://{SPIDER_PEP_URL}/']

    def parse(self, response):
        pep_tr_tags = response.css('section tbody tr')
        for pep_tr_tag in pep_tr_tags:
            pep_link = pep_tr_tag.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css('title::text').get().rstrip(END_NAME)
        data_list = pep_info.split(MID_SEP)
        number = data_list[0].lstrip(START_NAME)
        name = data_list[1]
        data = {
            'number': number,
            'name': name.strip(),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
