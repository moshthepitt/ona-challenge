import requests
from collections import Counter


def get_request(url):
    request = requests.get(url)
    return request


def get_data(url):
    request = get_request(url)
    return request.json()


def calculate(url):
    data = get_data(url)
    # the counters are used to, well, keep count of communities
    # and enable easy/efficient ranking
    points_not_working = Counter()
    points_working = Counter()
    points_unknown = Counter()
    points_all = Counter()

    for i in data:
        this_community = i['communities_villages']
        status = i['water_functioning']
        points_all[this_community] += 1
        if status == "yes":
            points_working[this_community] += 1
        elif status == "no":
            points_not_working[this_community] += 1
        else:
            points_unknown[this_community] += 1

    total_not_working = sum(points_not_working.values())

    points_not_working_percentage = [{x: y / total_not_working} for x, y in points_not_working.most_common()]

    result = {
        'number_functional': sum(points_working.values()),
        'number_water_points': points_all.most_common(),
        'community_ranking': points_not_working_percentage
    }
    return result


def percent_water_functioning_by(url, bool_key, split_key):
    result = {}
    data = get_data(url)
    holder = {}
    for i in data:
        bool_key_value = i[bool_key]
        split_key_value = i[split_key]
        if split_key_value not in holder:
            holder[split_key_value] = {"sum": 0}
        if bool_key_value not in holder[split_key_value]:
            holder[split_key_value][bool_key_value] = 0
        holder[split_key_value][bool_key_value] += 1
        holder[split_key_value]["sum"] += 1
    # so now we have a holder dict
    # e.g. {'some_val': {'yes': 12, 'no': 8, 'sum': 20} ... }
    for key, val in holder.items():
        inner_results = {}
        for key1, val1 in val.items():
            if key1 != "sum":
                perc = (val1 / val["sum"]) * 100
                inner_results[key1] = perc
        result[key] = inner_results
    return result
