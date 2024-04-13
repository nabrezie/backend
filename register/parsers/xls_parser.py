import pandas as pd


class XLSXtoJSONParser:
    """A class to parse XLSX files to JSON format.

        Attributes:
            file_path (str): The file path of the XLSX file to be parsed.

        Methods:
            parse_xlsx_to_json(): Parses the XLSX file to JSON format.
        """
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_xlsx_to_json(self):
        # Read the Excel file into a DataFrame
        df = pd.read_excel(self.file_path)

        # Convert DataFrame to JSON format
        json_data = df.to_json(orient="records")

        return json_data

