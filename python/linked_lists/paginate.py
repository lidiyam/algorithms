
# Complete the function below.
def get_page(num, inputs):
    result = []
    skipped = []
    hosts = set()
    count = 0
    i = 0
    length = len(inputs)

    while count < num and i < length:
        row = inputs[i]
        host_id = row.split(',')[0]
        if host_id in hosts:
            skipped.append(row)
        else:
            result.append(row)
            hosts.add(host_id)
            count += 1
        i += 1

    while count < num and skipped:
        row = skipped.pop(0)
        result.append(row)
        count += 1

    skipped.extend(inputs[i:])
    return result, skipped


def paginate(num, results):
    result = []
    inputs = results

    while inputs:
        next_page, inputs = get_page(num, inputs)
        result.extend(next_page)
        result.append("")

    return result


def paginate2(num, results):
    host_ids = {}
    final = []

    for i in range(len(results)):
        row = results[i]
        host_id = row.split(',')[0]
        if host_id in host_ids.keys():
            lst = host_ids[host_id]
            host_ids[host_id] = lst.append(i)

    hosts = set()
    for row in results:
        host_id = row.split(',')[0]
        if host_id in hosts:
            continue
        else:
            final.append(row)
            host_ids[host_id] = host_ids[host_id].pop(0)

if __name__ == '__main__':
    num = 5
    input = [
        '1, 28, 310.6, SF',
        '4, 5, 204.1, SF',
        '20, 7, 203.2, Oakland',
        '6, 8, 202.2, SF',
        '6, 10, 199.1, SF',
        '1, 16, 190.4, SF',
        '6, 29, 185.2, SF',
        '7, 20, 180.1, SF',
        '6, 21, 162.1, SF',
        '2, 18, 161.2, SF',
        '2, 30, 149.1, SF',
        '3, 76, 146.2, SF',
        '2, 14, 141.1, San Jose'
    ]
    input2 = [
        "1,8,207.1,Melbourne",
        "1,10,206.1,Melbourne",
        "1,29,204.1,Melbourne",
        "1,21,202.1,Melbourne",
        "8,18,201.1,Melbourne",
        "8,30,200.1,Melbourne",
        "7,11,199.1,Melbourne"
    ]

    results = paginate(num, input)
    for page in results:
        print page