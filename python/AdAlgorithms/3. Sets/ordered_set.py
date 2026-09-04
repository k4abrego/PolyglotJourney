from typing import cast

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
        # TODO: Check if value already exists

        #Assume that values doesn't exist, so add to the end 
        self.__count += 1
        new_node: OrderedSet.Node(T) = OrderedSet.Node(value)
        new_node.prev: self.__sentinel.prev 
        new_node.next: self.__sentinel.next
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node
        

if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    a.add(4)
    a.add(8)
    a.add(15)
    a.add(16)
    a.add(23)
    print(len(a))