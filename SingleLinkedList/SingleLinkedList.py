from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
import timeit

T = TypeVar("T")

class IndexOutRangeException(Exception):
    pass


@dataclass
class SingleNode(Generic[T]):
    data: T
    next_ptr: Optional['SingleNode[T]'] = None


class SingleLinkedList:

    def __init__(self) -> None:
        self._length: int = 0
        self.__head: Optional[SingleNode[T]] = None
        self.__tail: Optional[SingleNode[T]] = None

    def __len__(self) -> int:
        return self._length

    def append(self, data: T) -> None:
        if not isinstance(data, SingleNode):
            data = SingleNode(data)
        if self.__head is None:
            self.__head = data
        else:
            self.__tail.next_ptr = data

        self.__tail = data
        self._length += 1

    def __str__(self) -> str:
        node: Optional[SingleNode[T]] = self.__head
        my_str: str = '['
        while node.next_ptr:
            my_str += f'{node.data}, '
            node = node.next_ptr
        my_str += f'{node.data}]'
        return my_str

    def is_empty(self) -> bool:
        return self._length == 0

    def insert(self, index: int, data: T) -> None:
        if index < 0 or index > self._length:
            raise IndexOutRangeException("Index is out of range")
    
        new_node: Optional[SingleNode[T]] = SingleNode(data)
    
        if index == 0:
            new_node.next_ptr = self.__head
            self.__head = new_node
            if self._length == 0:
                self.__tail = new_node
        else:
            prev_node: Optional[SingleNode[T]] = None
            curr_node: Optional[SingleNode[T]] = self.__head

            for i in range(index):
                prev_node = curr_node
                curr_node = curr_node.next_ptr

            new_node.next_ptr = curr_node
            prev_node.next_ptr = new_node

            if index == self._length:
                self.__tail = new_node

        self._length += 1

    def reverse(self) -> None:
        if self._length <= 1:
            return

        prev_node: Optional[SingleNode[T]] = None
        curr_node: Optional[SingleNode[T]] = self.__head
        next_node: Optional[SingleNode[T]] = curr_node.next_ptr

        while next_node is not None:
            curr_node.next_ptr = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next_ptr

        curr_node.next_ptr = prev_node
        self.__head = curr_node

    def contains(self, data: T) -> bool:
        node: Optional[SingleNode[T]] = self.__head
        while node is not None:
            if node.data == data:
                return True
            node = node.next_ptr
        return False

    def get(self, index: int) -> T:
        if index < 0 or index >= self._length:
            raise IndexOutRangeException("Index is out of range")
        current_node: Optional[SingleNode[T]] = self.__head
        for i in range(index):
            current_node = current_node.next_ptr
        return current_node.data

    def remove(self, index: int) -> None:
        if index < 0 or index >= self._length:
            raise IndexOutRangeException("Index is out of range")

        if index == 0:
            self.__head = self.__head.next_ptr
            if self._length == 1:
                self.__tail = None
        else:
            prev_node: Optional[SingleNode[T]] = None
            curr_node: Optional[SingleNode[T]] = self.__head

            for i in range(index):
                prev_node = curr_node
                curr_node = curr_node.next_ptr

            prev_node.next_ptr = curr_node.next_ptr

            if index == self._length - 1:
                self.__tail = prev_node

        self._length -= 1
    
    def get_head(self) -> Optional[SingleNode[T]]:
        return self.__head

    def search(self, node: Optional[SingleNode[T]], item: T) -> bool:
        if node == None:
            return False
        if node.data == item:
            return True
        return self.search(node.next_ptr, item)



linked_list = SingleLinkedList()
def benchmark_append():
    for i in range(0, 10000):
        linked_list.append(i)

print("Время выполнения функции append:", timeit.timeit(benchmark_append, number=1))

def benchmark_reverse():
    linked_list.reverse()
print("Время выполнения функции get:", timeit.timeit(benchmark_reverse, number=1))
