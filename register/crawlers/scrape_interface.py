"""
     This interface is used to scrape data from various sources. It provides a method to scrape data from a given source.

    Example usage:
    # interface.scrape_data(source="BusinessRegister", register="RPO", to_extract=KEYS, query="sync?last_id=2142424")

    # interface.scrape_data(source="SlovakStatistics", cube_code="np3106rr", params=["SK021", "2016,2017,2018", "E_PRIEM_HR_MZDA"], to_extract=['version', 'label'], lang="sk")


    Raises:
        NotImplementedError: _description_
        ValueError: _description_
"""
import scrapy
from scrapy.crawler import CrawlerProcess

class DataScraperInterface:
    def __init__(self):
        pass

    def scrape_data(self, source, **kwargs):
        raise NotImplementedError("Not implemented yet")


class BusinessRegisterSpider(scrapy.Spider):
    # Business Register Spider implementation...
    # Not implemented yet
    pass

class SlovakStatisticsSpider(scrapy.Spider):
    # Slovak Statistics Spider implementation...
    # Not implemented yet 
    pass

class DataScraper(DataScraperInterface):
    def __init__(self):
        super().__init__()

    def scrape_data(self, source, **kwargs):
        if source == "BusinessRegister":
            process = CrawlerProcess()
            process.crawl(BusinessRegisterSpider, **kwargs)
            process.start()
        elif source == "SlovakStatistics":
            process = CrawlerProcess()
            process.crawl(SlovakStatisticsSpider, **kwargs)
            process.start()
        else:
            raise ValueError("Invalid data source. Please provide either 'Obchodny register SR' or 'Statisticky urad SR'.")

if __name__ == "__main__":
    interface = DataScraper()

