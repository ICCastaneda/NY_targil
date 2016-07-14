class revstr(object):
    
    def __init__(self, data, *args, **kyws):
        self.data = data
        self.indx = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.indx == 0:
            raise StopIteration
        else:
            self.indx -= 1
            return self.data[self.indx]



def genrev(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]
