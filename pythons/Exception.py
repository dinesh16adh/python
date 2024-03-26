def test():
    try:
        a = "hello" + 1
    except TypeError as t:
        print(t)


test()
