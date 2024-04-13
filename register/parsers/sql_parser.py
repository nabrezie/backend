class JSONtoSQLParser:
    def __init__(self, json_data):
        self.json_data = json_data
        self.sql_queries = []

    def parse(self, table_name):
        self.parse_main_table(table_name)
        self.parse_nested_tables()

    def parse_main_table(self, table_name):
        main_table_columns = [key for key, value in self.json_data.items() if not isinstance(value, (dict, list))]
        main_table_sql = f"""
        INSERT INTO {table_name} ({', '.join(main_table_columns)})
        VALUES ({', '.join(['%s'] * len(main_table_columns))});
        """
        main_values = tuple(self.json_data.get(key) for key in main_table_columns)
        self.sql_queries.append((main_table_sql, main_values))

    def parse_nested_tables(self):
        nested_keys = [key for key, value in self.json_data.items() if isinstance(value, list)]
        for key in nested_keys:
            for entry in self.json_data[key]:
                table_name = key[:-8]  
                sql = f"""
                INSERT INTO {table_name} ({', '.join(entry.keys())})
                VALUES ({', '.join(['%s'] * len(entry))});
                """
                values = tuple(entry.values())
                self.sql_queries.append((sql, values))

    def generate_sql_queries(self, table_name="organizations"):
        self.parse(table_name)
        for query, values in self.sql_queries:
            print(query % values)


if __name__ == "__main__":
    json_data = {
        "id": 1665873,
        "established_on": "1800-01-01",
        "terminated_on": "1800-01-01",
        "actualized_at": None,
        "has_organization_unit": False,
        "has_operations": False,
        "random_nested_table": [
            {
                "id": 1,
                "name": "nested_table_1"
            },
            {
                "id": 2,
                "name": "nested_table_2"
            }
        ],
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

    parser.generate_sql_queries(table_name="kokot")
