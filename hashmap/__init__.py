__version__ = "0.1.0"

import typing
import collections.abc

_SENTINEL_VALUE = object()


class Pair(typing.NamedTuple):
    key: typing.Hashable
    value: typing.Any


class HashMap(collections.abc.MutableMapping):
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
        old_pairs = self._buckets
        self._size_factor += 1
        self._num_buckets = 2 ** self._size_factor - 1
        self._buckets = [None for _ in range(self._num_buckets)]
        self._length = 0

        for pair in old_pairs:
            if pair is None:
                continue
            self.set(pair.key, pair.value)

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

        Args:
            key (typing.Hashable): Any hashable value
            default (typing.Any, optional): A value to return if the given key
                doesn't exist. Defaults to None.

        Returns:
            typing.Any: The value from the HashMap for the given key, or the
                default value if it doesn't exist
        """
        pair = self._buckets[self._get_index(key)]
        if (pair is None) or (pair.key != key):
            if default == _SENTINEL_VALUE:
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
        pair = self._buckets[self._get_index(key)]
        if (pair is None) or (pair.key != key):
            raise KeyError(f"key does not exist: {key}")
        else:
            self._length -= 1
            self._buckets[self._get_index(key)] = None
            return pair.value

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        self.set(key, value)

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        return self.get(key)

    def __delitem__(self, key: typing.Hashable) -> None:
        self.delete(key)

    def __iter__(self) -> typing.Iterator[typing.Tuple[typing.Hashable, typing.Any]]:
        return (pair for pair in self._buckets if pair is not None)

    def __len__(self) -> int:
        return self._length
