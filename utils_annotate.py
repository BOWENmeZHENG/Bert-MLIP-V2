import json

def load_json(file):
    with open(file, "r") as f:
        data = json.loads(f.read())
    return data

def read_data(json_file, max_length):
    data_list = []
    with open(json_file) as f:
        for jsonObj in f:
            record = json.loads(jsonObj)
            if len(record['words']) > max_length:
                record['words'] = record['words'][:max_length]
                record['ner'] = record['ner'][:max_length]
            data_list.append(record)
    return data_list