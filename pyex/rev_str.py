import string

def singleton(cls, *args, **kyw):
    instances = {}
    def get_instance( *args, **kyw):
        if cls not in instances:
            instances[cls] = cls(*args, **kyw)
        return instances[cls]
    return get_instance


@singleton
class tsingleton(object):
    def __init__(self, *args, **kyw):
        self.count = 0
        print "args = {}, kyw = {}".format(args, kyw)

    def addcount(self):
        self.count += 1
        print "count = {}".format(str(self.count))     



def revstr(instr):
    print 'instr=', instr
    rstr = ""
    for indx in range((len(instr) - 1), -1, -1):
          rstr += str(instr[indx])
    print 'reverse str is:{}'.format(rstr)
    return rstr



def do_some_work():
    list1 = ['abcdefg', '1234567', 'good-work']
    for l1 in list1:
        revstr(l1)


    for indx in range(4):
        si = str(indx)
        x1 = tsingleton('aaa', 'bbbb', shalom='yes', moshe='no')
        x1.addcount()
        print "x1={}".format(repr(x1))
        x2 = tsingleton('aaa2', 'bbbb2', shalom='yes2', moshe='no2')
        x2.addcount()
        print "x2={}".format(repr(x2))
        
    return 'ok'



if __name__ == '__main__':
   do_some_work()
   print 'all work done'







 
