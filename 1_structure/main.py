from collections import deque
from typing import TextIO
import operator

print('========== 1.3 history (with generator)')

print('== simple iterator')


def iter_func(initial: int, max_length: int):
    value = initial
    count = 0
    while count < max_length:
        yield value
        count += 1
        value += 1
    raise StopIteration


iterator = iter_func(1, 5)
for i in range(1, 4):
    v = next(iterator)
    print(v)

print('== simple iterator')


def search(f: TextIO, pattern: str) -> deque:
    store = deque(maxlen=4)
    for line in f:
        if pattern in line:
            yield line, store
        store.append(line)


with open('some.txt', 'r') as f:
    for current, s in search(f, 'python'):
        print(current, s)

print('============ 1.5 prioty queue')

import heapq


class PQ:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        self._index += 1
        heapq.heappush(self._queue, (-priority, self._index, item))

    def pop(self):
        i = heapq.heappop(self._queue)[-1]
        print(i)


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


h = PQ()
h.push(Item('sadffda'), 1)

h.push(Item('asdf'), 3)
h.push(Item('wwwww'), 2)
h.pop()
h.pop()
h.pop()

print('=========== 1.8 calculate dictiornaly')

prices = {
    'a': 1,
    'b': 102,
    'c': 13,
    'd': 14,
}

inversed = zip(prices.values(), prices.keys())

print(max(inversed)[1])

print('=========== 1.13 one line getter =============')

dict_ = {1: 3}
item_getter = operator.itemgetter(1)
print(item_getter(dict_))
object_getter = operator.attrgetter('__class__')
print(object_getter(1))
caller = operator.methodcaller('__str__')
print(caller(1))

print('============= 1.16 filtering with generator')
gen = (print(i) for i in [1, 2, 3])
next(gen)
next(gen)
next(gen)

