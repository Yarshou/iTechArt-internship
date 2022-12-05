import json


def merge_students_data(csv_file, xlsx_workbook, json_file):
    next(csv_file)
    res_dict = {f'{v[0]} {v[1]}': {'age': int(v[2])} for v in [row.strip().split(',') for row in csv_file]}
    for name, *marks in xlsx_workbook.worksheets[0].values:
        res_dict[name]['marks'] = marks
    json.dump(res_dict, json_file)
