a = {'1':lambda :f}
def f():
    print 'hello'
a['1']()()
