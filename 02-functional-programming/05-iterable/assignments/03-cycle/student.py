import itertools


def cycle(xs):
    while True:
        for item in xs:
            yield item

         
        
        
xs = cycle('abcd')
itertools.islice(xs, 10)