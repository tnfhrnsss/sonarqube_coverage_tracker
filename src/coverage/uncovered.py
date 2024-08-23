
def find(components):
    keys = []
    key_dict = []
    for component in components:
        key = component['key']
        name = component['name']
        measures = component['measures']
        coverage = 0
        uncovered_line = 0
        for measure in measures:
            metric = measure['metric']
            value = float(measure['period']['value'])

            if metric == 'new_coverage':
                coverage = value
            elif metric == 'new_uncovered_lines':
                uncovered_line = value
        if coverage < 60.0 and uncovered_line >= 10:
            keys.append(key)
            entry = {'key': key, 'name': name, 'coverage': coverage}
            key_dict.append(entry)

    return key_dict


def validate(value):
    if value is not None:
        try:
            return float(value) < 60.0
        except ValueError:
            return False
    return False
