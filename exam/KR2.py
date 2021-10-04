import typing
import json


def xlsx_to_json(xlsx_workbook, json_file):
    res_dict = dict()
    for key, inner_key, *values in xlsx_workbook.worksheets[0].values:
        if key is None:
            res_dict[prev_key][inner_key] = values[0]
        else:
            res_dict[key] = {inner_key: values[0]}
            prev_key = key
    json.dump(res_dict, json_file)
