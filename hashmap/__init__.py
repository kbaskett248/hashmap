"""This file contains a pure python implementation of a Hash Map.

The HashMap is implemented as a list of buckets. Each bucket contains None or
a key-value pair. The number of buckets is computed based on a size factor. 
When the HashMap is initialized, the size factor is 10, and the number of 
buckets is 2^10 - 1, or 1023.

When a key-value pair is added to the HashMap, the key is hashed to an index in
the bucket list. If the bucket is empty (it contains None), then the key-value
pair is stored in the bucket. If the bucket is occupied, and the key coming in
matches the existing key, then the value is replaced. Otherwise the bucket is
occupied with a different key, indicating a hash conflict. In this case the 
HashMap is expanded by increasing the size factor by 1, doubling the number of 
buckets. All existing pairs are added to the list, and then the new pair is
added.

"""

__version__ = "1.0.0"

import typing
import collections.abc

_SENTINEL_VALUE = object()


class Pair(typing.NamedTuple):
    key: typing.Hashable
    value: typing.Any


class HashMap(collections.abc.MutableMapping):
    """A Pure Python implementation of a HashMap.

    Any hashable value may be used as the key, and it can point to any value.

    """

    _size_factor: int
    _num_buckets: int
    _length: int
    _buckets: typing.List[typing.Optional[Pair]]

    def __init__(self, *args, **kwargs):
        self._size_factor = 9
        self._buckets = []
        self._expand()
        self._length = 0

        for iterable in args:
            for key, value in iterable:
                self.set(key, value)

        for key, value in kwargs.items():
            self.set(key, value)

    def _get_index(self, key: typing.Hashable) -> int:
        """Convert a key to the corresponding index in buckets.

        Args:
            key (typing.Hashable): Any hashable value

        Returns:
            int: The index in buckets for the given key
        """
        return hash(key) % self._num_buckets

    def _expand(self):
        """Double the number of buckets available in the hashmap"""
        old_pairs = list(iter(self))
        self._size_factor += 1
        self._num_buckets = 2 ** self._size_factor - 1
        self._buckets = [None for _ in range(self._num_buckets)]
        self._length = 0

        for key, value in old_pairs:
            self.set(key, value)

    def set(self, key: typing.Hashable, value: typing.Any):
        """Set the value for key in the HashMap.

        Args:
            key (typing.Hashable): Any hashable value
            value (typing.Any): The value to associate with the given key
        """
        while True:
            index = self._get_index(key)
            pair = self._buckets[index]
            if pair is None:
                self._buckets[index] = Pair(key, value)
                self._length += 1
                break
            elif pair.key == key:
                self._buckets[index] = Pair(key, value)
                break
            else:
                self._expand()

    def get(self, key: typing.Hashable, default=_SENTINEL_VALUE) -> typing.Any:
        """Return the value for the given key.

        If the key isn't present in the HashMap, return a default value.
        If no default value was specified, raise a KeyError.

        Args:
            key (typing.Hashable): Any hashable value
            default (typing.Any, optional): A value to return if the given key
                doesn't exist.

        Raises:
            KeyError: A KeyError is raised if the specified key does not exist
                in the HashMap and no default was specified.

        Returns:
            typing.Any: The value from the HashMap for the given key, or the
                default value if it doesn't exist
        """
        pair = self._buckets[self._get_index(key)]
        if (pair is None) or (pair.key != key):
            if default is _SENTINEL_VALUE:
                raise KeyError(f"key does not exist: {key}")
            else:
                return default
        else:
            return pair.value

    def delete(self, key: typing.Hashable) -> typing.Any:
        """Delete the value for the given key from the HashMap.

        Args:
            key (typing.Hashable): Any hashable value

        Raises:
            KeyError: A KeyError is raised if the specified key does not exist
                in the HashMap.

        Returns:
            typing.Any: The value associated with the given key.
        """
        index = self._get_index(key)
        pair = self._buckets[index]
        if (pair is None) or (pair.key != key):
            raise KeyError(f"key does not exist: {key}")
        else:
            self._length -= 1
            self._buckets[index] = None
            return pair.value

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        """Set the value for key in the HashMap.

        Args:
            key (typing.Hashable): Any hashable value
            value (typing.Any): The value to associate with the given key
        """
        self.set(key, value)

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        """Return the value for the given key.

        If the key isn't present in the HashMap, raise a KeyError.

        Args:
            key (typing.Hashable): Any hashable value

        Raises:
            KeyError: A KeyError is raised if the specified key does not exist
                in the HashMap.

        Returns:
            typing.Any: The value from the HashMap for the given key
        """
        return self.get(key)

    def __delitem__(self, key: typing.Hashable) -> None:
        """Delete the value for the given key from the HashMap.

        Args:
            key (typing.Hashable): Any hashable value

        Raises:
            KeyError: A KeyError is raised if the specified key does not exist
                in the HashMap.
        """
        self.delete(key)

    def __iter__(self) -> typing.Iterator[typing.Tuple[typing.Hashable, typing.Any]]:
        """Return an iterator to iterate over the key-value pairs.

        Returns:
            typing.Iterator[typing.Tuple[typing.Hashable, typing.Any]]: An iterator
                over the key-value pairs in the HashMap
        """
        return (pair for pair in self._buckets if pair is not None)

    def __len__(self) -> int:
        """Return the number of items in the HashMap.

        Returns:
            int: A count of the number of items in the HashMap
        """
        return self._length

    def __str__(self) -> str:
        """Return a string representation of the HashMap.

        Returns:
            str: A string representation of the HashMap
        """
        contents = ", ".join(sorted(f"{key!r}: {value!r}" for key, value in self))
        return f"HashMap({contents})"


__all__ = ["HashMap"]
