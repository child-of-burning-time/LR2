from dataclasses import dataclass
import ctypes
from typing import TypeVar, Generic, Optional
import timeit


K = TypeVar("K", int, str)
V = TypeVar("V")


@dataclass
class HashTableEntry(Generic[K, V]):
    key: K
    value: V

class HashTable(Generic[K, V]):

    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._size: int = 0
        self._table: ctypes.Array[Optional[HashTableEntry[K, V]]] = (
            capacity * ctypes.py_object)()
        for i in range(0, capacity):
            self._table[i] = None

    def _hash(self, key: K) -> int:
        h = hash(key)
        return (self._capacity - 1) & (h ^ (h >> 16))

    def _find_entry(self, key: K) -> int:
        index: int = self._hash(key)

        while self._table[index] is not None:
            if self._table[index].key == key:
                return index

            index = (index + 1) % self._capacity

        return -1

    def size(self) -> int:
        return self._size

    def get(self, key: K) -> Optional[V]:
        index: int = self._find_entry(key)

        if index == -1:
            raise KeyError("Key not found")

        return self._table[index].value

    def put(self, key: K, value: V) -> None:
        index: int = self._find_entry(key)

        if index != -1:
            self._table[index].value = value
        else:
            entry: HashTableEntry[K, V] = HashTableEntry(key=key, value=value)
            index = self._hash(key)

            while self._table[index] is not None:
                index = (index + 1) % self._capacity

            self._table[index] = entry
            self._size += 1

        if self._size >= self._capacity * 0.75:
            self._resize(self._capacity * 2)

    def remove(self, key: K) -> None:
        index: int = self._find_entry(key)

        if index == -1:
            raise KeyError("Key not found")

        self._table[index] = None
        self._size -= 1

        if self._size <= self._capacity * 0.25:
            self._resize(self._capacity // 2)

    def __str__(self) -> str:
        my_str: str = ""
        for i in range(self._capacity):
            entry: Optional[HashTableEntry[K, V]] = self._table[i]
            if entry is not None:
                my_str += f"({entry.key}, {entry.value}) "

        return f"{my_str}"

    def _resize(self, new_capacity: int) -> None:
        new_table: ctypes.Array[Optional[HashTableEntry[K, V]]] = (
            new_capacity * ctypes.py_object)()
        for i in range(0, new_capacity):
            new_table[i] = None

        for i in range(self._capacity):
            entry: Optional[HashTableEntry[K, V]] = self._table[i]
            if entry is not None:
                index: int = self._hash(entry.key)

                while new_table[index] is not None:
                    index = (index + 1) % new_capacity

                new_table[index] = entry

        self._table = new_table
        self._capacity = new_capacity

    def contains(self, key: K) -> bool:
        index: int = self._find_entry(key)
        return index != -1



hash_table = HashTable(1000)
def benchmark_put():
    for i in range(1000):
        hash_table.put(i, i)

def benchmark_get():
    for i in range(1000):
        hash_table.get(i)

print("Время выполнения функции put:", timeit.timeit(benchmark_put, number=1))
print("Время выполнения функции get:", timeit.timeit(benchmark_get, number=1))
