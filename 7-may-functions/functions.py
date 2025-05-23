def fun1(*args):
    print(type(args))


def details(**args):
    print(type(args))


details(h=20,ycd =90)
fun1(10,20,30)