from collections.abc import Iterator

a: list[int] = [4, 8, 15, 16, 23, 42]
b: str = 'Hello'
c: tuple[float, ...] = (3.14, 2.91, 9.1)

for elem in a:
    print(elem)

print()

it1: Iterator[str] = iter(b)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it))

print()

it2: Iterator[float] = iter(c)
try:
    while True:
        print(next(it2))
except StopIteration:
    ...

print()

class CountDown:

    current: int

    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        result: int = self.current
        self.current -= 1
        return result

it3: Iterator[int] = CountDown(3)
print(next(it3))
print(next(it3))
print(next(it3))
print(next(it3))
# print(next(it3))

print()

for i in CountDown(10):
    print(i)

def generator_example() -> Iterator[int]:
    x: int = 1
    yield x
    x += 2
    yield x
    x *= 2
    yield x

print()

it4: Iterator[int] = generator_example()
print(next(it4))
print(next(it4))
print(next(it4))
# print(next(it4))

print()

for i in generator_example():
    print(i)

def count_down(start: int) -> Iterator[int]:
    while start >= 0:
        yield start
        start -= 1

print()

it5: Iterator[int] = count_down(3)
print(next(it5))
print(next(it5))
print(next(it5))
print(next(it5))
# print(next(it5))

print()

for i in count_down(10):
    print(i)