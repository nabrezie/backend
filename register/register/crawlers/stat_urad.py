import scrapy
from scrapy.crawler import CrawlerProcess

ALL_TABLES = "https://data.statistics.sk/api/v2/collection?lang=sk"
DEF_URL = "https://data.statistics.sk/api/v2/dataset/"        
KEYS = ['version', 'class', 'label', 'update', 'note', 'href', 'id', 'size', 'role', 'dimension', 'value']
class SlovakStatisticsSpider(scrapy.Spider):
    name = "slovak_statistics"
    
    ''' 
        Požiadavka na údaje má formu URL odkazu, ktorý vytvoríme podľa vzoru https://data.statistics.sk/api/v2/dataset/cube_code/PARAM1/PARAM2/PARAM3...?lang=lang_code&type=file_type, kde cube_code je osemmiestny kód tabuľky, PARAM1, PARAM2 .... sú kódy elementov dimenzií vybranej tabuľky, lang_code je kód jazyka (sk alebo en) – nepovinné (predvolené sk), file_type je typ súboru (json, csv, xml, xlsx, ods) – nepovinné (predvolené json). Na zostavenie linky môžete použiť formulár dostupný po kliknutí na detail tabuľky.
    '''

    def __init__(self, url=DEF_URL,
                 cube_code=None,
                 params=[],
                 to_extract=[],
                 lang="sk",
                 type="json",
                 *args,
                 **kwargs):
        super(SlovakStatisticsSpider, self).__init__(*args, **kwargs)
        if url == ALL_TABLES:
            self.start_url = url
        else:
            self.start_url = url + self.generate_url(cube_code, params, lang, type)
        self.to_extract = to_extract

    def generate_url(self, cube_code, params, lang, type):
        """ Generates a URL for the request

        Args:
            cube_code (_type_): table code
            params (_type_): list of parameters
            lang (_type_): language code ("sk" or "en") 
            type (_type_): Maybe useless because the default is json on the website

        Returns:
            _type_: _description_
        """
        generated = ""

        if cube_code is not None:
            generated = f"{cube_code}/"
        if len(params) > 0:
            generated += "/".join(params)
        generated += f"/7?lang={lang}"
        # generated += f"&type={type}"
        return generated 

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)
    
    def extract_table(self, data) -> list:
        """Extracts useful info from a table

        Args:
            data (json): data to extract the table from
            params (list, optional): Information to extract - check KEYS. Defaults to [].
        """
        # href = data.get("href", "")
        # label = data.get("label", "")
        # update = data.get("update", "")
        # dimensions = data.get("dimension", "")

        # print("href:", href)
        # print("label:", label)
        # print("last Updated:", update)
        table = []
        for param in self.to_extract:
            table.append(data.get(param, "UNDEFINED"))
        return table
        # for _, dim_value in dimensions.items():
        #     dim_label = dim_value.get("label", "")
        #     dim_note = dim_value.get("note", "")
        #     dim_href = dim_value.get("href", "")
        #     print("dimension label:", dim_label)
        #     print("dimension note:", dim_note)
        #     print("dimension href:", dim_href)
        #     print("\n")

    def parse_all_tables(self, response):
        """Should parse a list of every table available at ALL_TABLES

        Args:
            response (_type_): response from the request
        """
        data = response.json()
        datasets = data.get("link", {}).get("item", [])
        for dataset in datasets:
            extracted = self.extract_table(dataset)
            print(extracted)

    def parse(self, response):
        """ Parse response

        Args:
            response (): response from the request
        """
        data = response.json()
        if response.url == ALL_TABLES:
            extracted = self.parse_all_tables(response)
        else:
            extracted = self.extract_table(data)
        print(extracted)

    
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(SlovakStatisticsSpider,
                  cube_code="np3106rr",
                  params=["SK021", "2016,2017,2018", "E_PRIEM_HR_MZDA"],
                  to_extract=['version', 'label'],
                  lang="sk",
                  )
    # process.crawl(SlovakStatisticsSpider, url=ALL_TABLES, to_extract=["href", "label"])
    process.start()

