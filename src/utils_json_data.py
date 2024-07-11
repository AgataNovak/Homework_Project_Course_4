import json
import os


def get_json_data(path_to_json):
    """Функция получения данных из JSON файла"""

    try:
        with open(path_to_json, "r") as json_data_file:
            data = json.load(json_data_file)
            return data
    except FileNotFoundError:
        return []


path_to_json = os.path.abspath("../data/products.json")
print(get_json_data(path_to_json))
