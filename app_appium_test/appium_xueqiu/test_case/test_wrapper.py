from functools import wraps


def f(a):
    def extend(fuc):
        @wraps(fuc)
        def hello(*args,**kwargs):
            print(a)
            print("hello")
            print(args)
            print(kwargs)
            fuc(*args,**kwargs)
            print("good bye")
        return hello
    return extend

@f("AAAAAAAA")
def tmp():
    # print("hello")
    print("tmp")
    # print("good bye")

# @extend
def tmp1():
    # print("hello")
    print("tmp1")
    # print("good bye")

def test_wrapper():
    # tmp(1,2,3,d=4)
    print(tmp())
    # tmp1()
    # extend(tmp)()
    # extend(tmp1)()