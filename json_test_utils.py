"""
Example:

>>> expected_json_obj = json_loads_with_matchers('''{
...     "any_value_is_accepted": ""ANY"",
...     "the_value_should_contain_the_substring": ""CONTAINS""{"my_substring"}
... }''')

>>> actual_json_obj = {
...     "any_value_is_accepted": 1234,
...     "the_value_should_contain_the_substring": "here is my_substring in this text",
... }

>>> assert expected_json_obj == actual_json_obj
"""

import json
from unittest.mock import ANY


def json_loads_with_matchers(json_string_with_templates: str, object_hook=None):
    ANY_TEMPLATE = '""ANY""'
    ANY_OBJ = {'__ANY__': {}}
    ANY_JSON = json.dumps(ANY_OBJ)
    
    object_hook = object_hook or (lambda _: _)

    return json.loads(
        json_string_with_templates
            .replace(ANY_TEMPLATE, ANY_JSON)
            .replace(ContainsMatcher.TEMPLATE, ContainsMatcher.JSON),
        object_hook=lambda obj:
            ANY if obj == ANY_OBJ else
            ContainsMatcher(obj) if ContainsMatcher.is_represented_by(obj) else
            object_hook(obj)
    )

  
class ContainsMatcher:
    TEMPLATE = '""CONTAINS""{'
    KEY = '__CONTAINS__'
    JSON = f'{{"{KEY}":'

    @classmethod
    def is_represented_by(cls, obj: dict) -> bool:
        return cls.KEY in obj

    def __init__(self, representation: dict):
        self.substring = representation[self.KEY]

    def __eq__(self, other: str) -> bool:
        return self.substring in other
