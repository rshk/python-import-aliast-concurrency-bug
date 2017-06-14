from multiprocessing.pool import ThreadPool

def do_stuff(*args, **kwargs):
    from foobar import somefunction

pool = ThreadPool(2)
pool.map(do_stuff, range(100))
