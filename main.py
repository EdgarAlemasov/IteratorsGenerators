# Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class ListIter(list):

    def __iter__(self):
        self.cursor = 0
        self.value = -1
        return self

    def __next__(self):
        if len(self) > self.cursor:
            self.value += 1
            if len(self[self.cursor]) > self.value:
                return self[self.cursor][self.value]
            else:
                self.cursor += 1
                self.value = -1
                return self.__next__()
        else:
            raise StopIteration


for item in ListIter(nested_list):
    print(item)

flat_list = [item for item in ListIter(nested_list)]
print(flat_list)


# Написать генератор, который принимает список списков, и возвращает их плоское представление.
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]


def get_item(list):
    cursor = 0
    value = 0
    while len(list) != cursor:
        while len(list[cursor]) != value:
            yield list[cursor][value]
            value += 1
        cursor += 1
        value = 0


for item in get_item(nested_list):
    print(item)


# Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    [[2]]
]


class ListIter2:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.value_stack = [iter(self.nested_list)]
        return self

    def __next__(self):
        while self.value_stack:
            try:
                value = next(self.value_stack[-1])
            except StopIteration:
                self.value_stack.pop()
                continue
            if isinstance(value, list):
                self.value_stack.append(iter(value))
                continue
            else:
                return value
        raise StopIteration


for item in ListIter2(nested_list):
    print(item)

flat_list = [item for item in ListIter2(nested_list)]
print(flat_list)


# Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]


def generator_nested_list(nested_list):
    for value in nested_list:
        if isinstance(value, list):
            for item in value:
                yield item
        else:
            yield value


for item in generator_nested_list(nested_list):
    print(item)