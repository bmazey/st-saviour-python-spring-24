import re
import json

if __name__ == '__main__':
    # https://docs.python.org/3/library/re.html

    # create a regular expression
    # expression = re.compile('ab.*')

    # check to see if provided text contains the pattern
    # print(expression.match('abab'))

    # dictionaries in python
    id = {
        'name': 'jane doe',
        'city': 'chicago',
        'age': '22'
    }

    # add an extra key / value pair
    id['phone'] = '605-477-3018'

    # duplicates not allowed!

    print(id['name'])

    # meet my friend json
    id = json.loads('{\"name\":\"john doe\",\"city\":\"chicago\",\"age\":\"22\"}')
    print(json.dumps(id))
