from decor_hw_2 import logger


@logger('logs3')
def flat_generator(some_list):
    for element in some_list:
        if isinstance(element, list):
            yield from flat_generator(element)
        else:
            yield element


nested_list = [
    [1, [2, [3]]],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)
