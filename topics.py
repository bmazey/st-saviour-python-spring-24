import re
import json

# recursive fibonacci
def fibonacci(n: int) -> int:
    """computes the nth number in the fibonacci sequence"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# dynamic fibonacci
def dynamic_fibonacci(n: int) -> int:
    """computes the nth number in the fibonacci sequence"""
    if n <= 1:
        return 1

    # create list to store computations
    dynamic = [1, 1]

    for i in range (2, n):
        dynamic.append(dynamic[i - 1] + dynamic[i - 2])

    return dynamic[n - 1]

if __name__ == '__main__':
    # fibonacci examples
    # print('recursive fibonacci: ' + str(fibonacci(40)))
    print('dynamic fibonacci: ' + str(dynamic_fibonacci(100)))

    # https://docs.python.org/3/library/re.html
    # create a regular expression
    # expression = re.compile('ab.*')

    # check to see if provided text contains the pattern
    # print(expression.match('abab'))

    # dictionaries in python
    jane_id = {
        'name': 'jane doe',
        'city': 'chicago',
        'age': '24'
    }

    # add an extra key / value pair
    jane_id['phone'] = '605-477-3018'
    # print(jane_id['phone'])

    # duplicates not allowed!

    # print(jane_id['name'])

    # meet my friend json
    john_id = json.loads('{\"name\":\"john doe\",\"city\":\"chicago\",\"age\":\"22\"}')
    # print(json.dumps(john_id))
    # print(john_id['city'])
