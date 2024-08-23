
def execute(targets):
    lines = []
    for target in targets:
        source = target['source']
        coverage = target['coverage']
        for key, value in source.items():
            line = f'{key},   Coverage: {coverage}%,  Author: @{value}\n'
            lines.append(line)
        message = ''.join(lines)
    return message

