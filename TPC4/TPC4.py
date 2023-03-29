import re
import json

def process_list(line):
    return [int(m) for m in re.findall(r"\d+", line)]

def operation(lst, operation_type):
    if operation_type == "media":
        return sum(lst) / len(lst)
    elif operation_type == "sum":
        return sum(lst)

def parse_header(header):
    param_lists = {}
    param_operations = {}

    for i, item in enumerate(header):
        match = re.search(r"(\w+)\{(\d+)(?:,(\d+))?\}(?:::(\w+))?", item)
        if match:
            header[i] = match.group(1) # extract parameter name
            if match.group(3) is None: # is it a list or a capture group?
                param_lists[header[i]] = (int(match.group(2)), None) # list 
            else:
                param_lists[header[i]] = (int(match.group(2)), int(match.group(3))) # capture group

            if match.group(4) is not None: # if it has an operation
                param_operations[header[i]] = match.group(4)

    return header, param_lists, param_operations

def parse_csv(csv):
    header, *lines = [s.strip() for s in csv.splitlines()]

    header, param_lists, param_operations = parse_header(header.split(','))
    
    regex = ""
    last = False

    for item in header:
        if item in param_lists:
            last = True

            quantity = f"{{{str(param_lists[item][0])}{'' if param_lists[item][1] is None else ','+ str(param_lists[item][1])}}}"
            regex += f"(?P<{item}>([^,;]+[,;]?){quantity})"
        else:
            last = False
            regex += rf"(?P<{item}>[^,;]+)[,;]"

    # Remove last commas and add new line
    if not last:
        regex = regex[:-4]

    data = []
    for line in lines:
        matches = re.finditer(regex, line)
        for match in matches:
            data += [match.groupdict()]

    for i in range(0, len(data)):
        for k in data[i]:
            if k in param_lists:
                data[i][k] = process_list(data[i][k])
            if k in param_operations:
                data[i][k] = operation(data[i][k], param_operations[k])

    for k in param_operations:
        for i in range(0, len(data)):
            data[i][f"{k}_{param_operations[k]}"] = data[i][k]
            del data[i][k]

    return data

def csv_to_json(src_file, dest_file):
    with open(src_file) as f:
        csv = f.read()

    data = parse_csv(csv)

    with open(dest_file, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

csv_to_json("csv/teste1.csv", "json/teste1.json")
csv_to_json("csv/teste2.csv", "json/teste2.json")
csv_to_json("csv/teste3.csv", "json/teste3.json")
csv_to_json("csv/teste4.csv", "json/teste4.json")
csv_to_json("csv/teste5.csv", "json/teste5.json")
