import scrapy
import json
from scrapy.crawler import CrawlerProcess
"""
    Tento modul berie data z obchodneho registra a spracovava ich do tabuliek
    - register pravnickych osob
    - centralny register zmluv
    - obchodny vestnik

    Na kulturne subjekty useless, ale ked to ma byt univerzalne riesenie na akykolvek zber dat, tak nech to tam je
    - register uctovnych zavierok 
    - dlznici socialnej poistovne
    - dlznici vseobecnej zdravotnej poistovne 

"""

# URLS
DEF_URL = "https://datahub.ekosystem.slovensko.digital/api/data/"

CENTR_REG_ZMLUV = "crz/contracts/" # CRZ
REG_PRAV_OSOB = "rpo/organizations/" # RPO 
OBCH_VESTNIK = "ov/bulletin_issues/" # OV
REG_UCT_ZAV = "ruz/accounting_entities/" # RUZ
DLZ_SOC_POIST = "socpoist/debtors/" # DSP
DLZ_VSEOB_ZDR_POIST = "vszp/debtors/" # DVZP


URLS = {
    "CRZ": CENTR_REG_ZMLUV,
    "RPO": REG_PRAV_OSOB,
    "OV": OBCH_VESTNIK,
    "RUZ": REG_UCT_ZAV,
    "DSP": DLZ_SOC_POIST,
    "DVZP": DLZ_VSEOB_ZDR_POIST
}

KEYS = ['id', 'established_on', 'terminated_on', 'actualized_at', 'has_organization_unit', 'has_operations', 'statistical_codes_actualized_on', 'created_at', 'updated_at', 'source_register', 'main_organization_id', 'deleted_at', 'registration_office_entries', 'registration_number_entries', 'identifier_entries', 'address_entries', 'alternate_name_entries', 'authorization_entries', 'deposit_entries', 'economic_activity_entries', 'equity_entries', 'legal_form_entries', 'legal_status_entries', 'name_entries', 'other_legal_fact_entries', 'predecessor_entries', 'share_entries', 'stakeholder_entries', 'statutory_entries', 'successor_entries']



class BusinessRegisterSpider(scrapy.Spider):
    name = "obchodny_register"

    def __init__(self, url=DEF_URL,
                 register=None,
                 query=None,
                 to_extract = [],
                 **kwargs):
        super().__init__(**kwargs)
        try:
            self.start_url = url + URLS[register] + query
        except Exception:
            if register is None:
                print("No register specified") 
            if query is None:
                print("Accessing with an empty query")
            return
        self.to_extract = to_extract
    
    def start_requests(self):
        """ Starts the request

        """
        yield scrapy.Request(url=self.start_url, callback=self.parse)

     # handling data
    def extract_table(self, data: dict, params=[]) -> dict:
        """Extracts useful info from a table and returns it as a dictionary

        Args:
            data (dict): given data
            params (list, optional): Information to extract - check KEYS. Defaults to [].

        Returns:
            dict: Extracted info {param: value}
        """
        table = {} 
        for param in params:
            item = data.get(param, "UNDEFINED")
            table[param] = item
        return table 

    def parse(self, response) -> list:
        """Parses the response and returns the extracted data

        Args:
            response (_type_): Response 

        Returns:
            list: Extracted data
        """
        if response.status != 200:
            print("Error with the response, status code:", response.status)
            return
        data = response.json() 
        extracted_data = []
        for d in data:
            extracted = self.extract_table(d, self.to_extract)
            extracted_data.append(extracted)
        self.save_parsed_data(extracted_data)

    def save_parsed_data(self, data: list):
        """Saves the parsed data to a file

        Args:
            data (list): Parsed data
        """
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BusinessRegisterSpider,
                  register="RPO",
                  to_extract=KEYS,
                  query="sync?last_id=2142424")
    process.start()