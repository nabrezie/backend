class JSONtoSQLParser:
    def __init__(self, json_data):
        """ Initializes the JSON to SQL parser

        Args:
            json_data (_type_): json data to parse
        """
        self.json_data = json_data
        self.sql_queries = []

    def parse(self, table_name):
        """ Parses the JSON data

        Args:
            table_name (_type_): the main table name in the database
        """
        self.parse_main_table(table_name)
        self.parse_nested_tables()

    def parse_main_table(self, table_name):
        """ Parses the main table from the JSON data

        Args:
            table_name (_type_): the main table name in the database
        """
        main_table_columns = [key for key, value in self.json_data.items() if not isinstance(value, (dict, list))]
        main_table_sql = f"INSERT INTO {table_name} ({', '.join(main_table_columns)}) VALUES ({', '.join(['%s'] * len(main_table_columns))});"
        main_values = tuple(self.json_data.get(key) for key in main_table_columns)
        self.sql_queries.append((main_table_sql, main_values))

    def parse_nested_tables(self):
        """ Parses the nested tables from the JSON data if any
        """
        nested_keys = [key for key, value in self.json_data.items() if isinstance(value, list)]
        for key in nested_keys:
            for entry in self.json_data[key]:
                table_name = key 
                sql = f"INSERT INTO {table_name} ({', '.join(entry.keys())}) VALUES ({', '.join(['%s'] * len(entry))});"
                values = tuple(entry.values())
                self.sql_queries.append((sql, values))

    def generate_sql_queries(self, table_name="organizations") -> list:
        """ Generates the SQL queries

        Args:
            table_name (str, optional): the main table name. Defaults to "organizations".

        Returns:
            (list): SQL queries as a list
        """
        self.parse(table_name)
        return self.sql_queries


# Define your JSON data
json_data = {
    "id": 1665873,
    "established_on": "1800-01-01",
    "terminated_on": "1800-01-01",
    "actualized_at": None,
    "has_organization_unit": False,
    "has_operations": False,
    "address_entries": [
        {
            "id": 503383,
            "organization_id": 1665873,
            "formatted_address": None,
            "street": "Párovská ul",
            "reg_number": 0,
            "building_number": ".",
            "postal_code": None,
            "municipality": "Pata",
            "country": "Slovenská republika",
            "effective_from": "1800-01-01",
            "effective_to": "1800-01-01",
            "created_at": "2016-05-15T07:40:51.021723Z",
            "updated_at": "2016-05-15T07:40:51.021723Z",
            "district": None
        }
    ],
    "economic_activity_entries": [
        {
            "id": 3801578,
            "organization_id": 1665873,
            "description": "Nákup a predaj potravín,alko-nealko nápojov v orig.balení.",
            "effective_from": "1800-01-01",
            "effective_to": "1800-01-01",
            "created_at": "2016-05-15T07:40:51.022992Z",
            "updated_at": "2016-05-15T07:40:51.022992Z",
            "suspended_from": None,
            "suspended_to": None
        }
    ],
    "name_entries": [
        {
            "id": 404445,
            "organization_id": 1665873,
            "name": "Helena Meszárošová - prevádzkareň",
            "effective_from": "1800-01-01",
            "effective_to": "1800-01-01",
            "created_at": "2016-05-15T07:40:51.020505Z",
            "updated_at": "2016-05-15T07:40:51.020505Z"
        }
    ]
}

parser = JSONtoSQLParser(json_data)

query = parser.generate_sql_queries(table_name="some_table_name")
print(query)
