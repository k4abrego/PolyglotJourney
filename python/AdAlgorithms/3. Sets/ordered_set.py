from typing import cast
from collections.abc import Iterator, Iterable

class OrderedSet[T]:

    class Node[N]:
        info: N
        next: OrderedSet.Node[N]
        prev: OrderedSet.Node[N]

        #Complexity: O(1)
        def __int__ (self, value: N) -> None:
            self.info = self
            self.next = self
            self.prev = self

    __sentinel: OrderedSet.Node[T] #special node that allows works with the nullpointer
    __count: int

    #Complexity: O(1)
    def __init__(self) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0 

#len()
    #Complexity: O(1)
    def __repr__(self) -> int:
        return  self.__count

    #Complexity: O(N)
    def __repr__(self) -> str:
        current: OrderedSet.Node[T] = self.__sentinel.next
        result: list[T] = []
        while current is not self.__sentinel:
            result.append(current.info)
            current = current.next
        return f'OrderedSet({result})' #list with all the items

#add
    #Complexity: O(1)
    def add(self, value: T) -> None:
        if value in self:
            return
        #Assume that values doesn't exist, so add to the end 
        self.__count += 1
        new_node: OrderedSet.Node[T] = OrderedSet.Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield current.info
            current = current.next

    # Complexity: O(N)
    def __contains__(self, value: object) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    a.add(4)
    a.add(8)
    a.add(15)
    a.add(16)
    a.add(23)

    print(len(a))

    it: Iterator[int] = iter(a)
    print(next(it))
    print(next(it))
    print()
    for i in a:
        print(i)
    b: OrderedSet[str] = OrderedSet('hello')
    print(b)