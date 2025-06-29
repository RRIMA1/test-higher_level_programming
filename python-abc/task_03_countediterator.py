class CountedIterator:    
    def __init__(self,iterable):
        self._iterator=iter(iterable)
        self._cptr=0
    
    def get_count(self):
        return self._cptr
    
    def __next__(self):
        try:
            next_item = next(self._iterator)
            self._cptr += 1
            return next_item
        except StopIteration:
            raise