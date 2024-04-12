from bs4 import BeautifulSoup
import requests
import scrapy


class HtmlScraper(scrapy.Spider):
    """Html scraper class"""
    name = 'htmlscraper'

    def __init__(self, url=None, *args, **kwargs):
        """Initialize.

        :param url: URL to scrape,
        :param args: Additional arguments,
        :param kwargs: Additional keyword arguments.
        :rtype: None.
        """
        super(HtmlScraper, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        """Parse response.

        :param response: Response object.
        :rtype: None.
        """
        title = response.xpath('//title/text()').get()
        print("Title:", title)


RMNO = "https://www.minv.sk/?register-mimovladnych-neziskovych-organizacii"
obch_reg = "https://www.orsr.sk/"
finstat = "https://www.finstat.sk/"
stat_urad = "https://slovak.statistics.sk/wps/portal/ext/home/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziA809LZycDB0NLPyCXA08QxwD3IO8TAwNTEz1wwkpiAJKG-AAjgZA_VFgJc7ujh4m5j4GBhY-7qYGno4eoUGWgcbGBo7GUAV4zCjIjTDIdFRUBADse0bP/dz/d5/L2dBISEvZ0FBIS9nQSEh/"

soup = BeautifulSoup(requests.get(RMNO).content, "html.parser")
print(soup.get_text())
