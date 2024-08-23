import requests
import uncovered
import source
from config_loader import config


def findAll(componentKey):
    api_url = config.get('sonarqube.api_url') + "/measures/component_tree?additionalFields=metrics&ps=500&asc=true&metricSort=new_coverage&s=metricPeriod&metricSortFilter=withMeasuresOnly&metricPeriodSort=1&component=" + componentKey + "&metricKeys=new_coverage%2Cnew_uncovered_lines%2Cnew_uncovered_conditions&strategy=leaves"
    response = requests.get(api_url)
    if response.status_code == 200:
        try:
            data = response.json()
            components = data['components']
            result = []
            if components is not None:
                size = len(components)
                if size > 0:
                    targets = uncovered.find(components)
                    for target in targets:
                        key = target['key']
                        name = target['name']
                        coverage = target['coverage']
                        source_info = source.find(key, name)
                        if source_info != {}:
                            source_entry = {'source': source_info, 'coverage': coverage}
                            result.append(source_entry)
            return result
        except ValueError:
            print("Response cannot be parsed as JSON")
    else:
        print(f"Request failed with status {response.status_code}")
        data = response.json()
        print("response - {} ".format(data))
