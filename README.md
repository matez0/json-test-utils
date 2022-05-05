# Utils for checking JSON values in tests


## Example

```python
>>> from json_test_utils import json_loads_with_matchers

>>> expected_json_obj = json_loads_with_matchers('''{
...     "any_value_is_accepted": ""ANY"",
...     "the_value_should_contain_the_substring": ""CONTAINS""{"my_substring"}
... }''')

>>> actual_json_obj = {
...     "any_value_is_accepted": 1234,
...     "the_value_should_contain_the_substring": "here is my_substring in this text",
... }

>>> assert expected_json_obj == actual_json_obj
```
