"""Original case templates with independently supplied expected results."""
import copy
import re

TEMPLATES = [('evaluate explicit required and forbidden response text', {'response': 'hello world', 'contains': ['hello'], 'excludes': ['secret']}, {'passed': True, 'checks': [{'kind': 'contains', 'value': 'hello', 'passed': True}, {'kind': 'excludes', 'value': 'secret', 'passed': True}]}), ('report a failed required-text assertion without calling a model', {'response': 'hello', 'contains': ['absent'], 'excludes': []}, {'passed': False, 'checks': [{'kind': 'contains', 'value': 'absent', 'passed': False}]}), ('accept an explicitly present JSON key with a null value', {'response': '{"a":null}', 'contains': [], 'excludes': [], 'json_keys': ['a']}, {'passed': True, 'checks': [{'kind': 'json_key', 'value': 'a', 'passed': True}]}), ('mark invalid recorded JSON as an assertion failure', {'response': 'oops', 'contains': [], 'excludes': [], 'json_keys': ['a']}, {'passed': False, 'checks': [{'kind': 'json_key', 'value': 'a', 'passed': False}]}), ('require a recorded response string', {'response': {}, 'contains': [], 'excludes': []}, None)]


def make_case(index):
    description, source, expected = copy.deepcopy(TEMPLATES[index % len(TEMPLATES)])
    def fill(value):
        if isinstance(value, str):
            if re.fullmatch(r"@i[+]\d+", value):
                return index + int(value[3:])
            return value.replace("{n}", str(index))
        if isinstance(value, list):
            return [fill(item) for item in value]
        if isinstance(value, dict):
            return {fill(key): fill(item) for key, item in value.items()}
        return value
    case = {"id": "prompts-{:04d}".format(index), "description": description, "input": fill(source)}
    case.update({"expected_error": True} if expected is None else {"expected": fill(expected)})
    return case
