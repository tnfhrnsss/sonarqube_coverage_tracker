import requests
from config_loader import config


def find(key, name):
    api_url = config.get('sonarqube.api_url')+ "/sources/lines?key="
    response = requests.get(api_url + key)
    if response.status_code == 200:
        try:
            data = response.json()
            sources = data['sources']
            if sources is not None:
                size = len(sources)
                if size > 0:
                    return filter(sources, name)
        except ValueError:
            print("Response cannot be parsed as JSON")
    else:
        print(f"Request failed with status {response.status_code}")
        data = response.json()
        print("response - {} ".format(data))


def filter(sources, name):
    target = {}
    for source in sources:
        isNew = source['isNew']
        if isNew & ('lineHits' in source):
            author = source['scmAuthor']
            target[name] = getAuthorId(author)
            break
    return target


def getAuthorId(author):
    try:
        return author.split('@')[0]
    except Exception as e:
        return author
