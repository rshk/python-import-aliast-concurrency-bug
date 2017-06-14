# Python 3,6 import-alias-concurrency-bug

Code to reproduce a bug in Python 3.6

Using the following code in concurrent code will fail:

```python
import package.module as _alias
```

While the following just works fine:

```python
from package import module as _alias
```

or even just

```python
import package.module
```


## How to reproduce

From a clone of the repo:

```
% python3.6 foo.py 
Traceback (most recent call last):
  File "foo.py", line 7, in <module>
    pool.map(do_stuff, range(100))
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 260, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 608, in get
    raise self._value
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 119, in worker
    result = (True, func(*args, **kwds))
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 44, in mapstar
    return list(map(*args))
  File "foo.py", line 4, in do_stuff
    from foobar import somefunction
  File "/tmp/tmp.K5XNcFjb5m/foobar/__init__.py", line 1, in <module>
    import foobar.submodule as foo
AttributeError: module 'foobar' has no attribute 'submodule'
```

## Affected versions

- python3.6 seems to be affected (3.6.1 on Archlinux; official Python docker image)
- python3.5 seems to be immune
