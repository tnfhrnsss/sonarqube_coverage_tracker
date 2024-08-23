import measure
import message_formatter
import slack_api
from config_loader import config


def execute():
    try:
        projects = config.get('projects')
        for project in projects:
            targets = measure.findAll(project)
            if len(targets) > 0:
                slack_api.send(project, message_formatter.execute(targets))
    except Exception as e:
        print("occur exception.!!", e)


execute()
